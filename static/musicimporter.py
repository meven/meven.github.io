#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Helps you organize music files efficiently
# Copyright (c)
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from os import listdir, makedirs, walk, makedirs, rmdir, remove #, renames
from os.path import isdir, dirname, basename, join
from shutil import copy,move
from sets import Set

try:
  # for mp3 support
  from mutagen.id3 import ID3, ID3NoHeaderError

  # for ogg support
  from mutagen.oggvorbis import OggVorbis

  # for flac support
  from mutagen.flac import FLAC

except ImportError:
  print "mutagen python library is necessary for this script"
  exit()

from optparse import OptionParser

usage = "usage: %prog [options] src_dir... output_dir"
parser = OptionParser(usage=usage)

parser.description = """moves and renames audio files cleaning files metadata. It supports mp3 Ogg Vorbis and Flac"""

#parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False)
parser.add_option("-w", "--write", action="store_true", dest="write", help="clean metadata of mp3 files, delete ID3v1 tags in favor of ID3v2.4", default=False)
parser.add_option("-m", "--move", action="store_true", dest="move", help="move files", default=False)
parser.add_option("-c", "--copy", action="store_true", dest="copy", help="copy files before processing", default=False)
parser.add_option("-d", "--delete-src-dir", action="store_true", dest="delsrcdir", help="delete the source dir after having moved the files", default=False)
parser.add_option("-o", "--output-format", dest="output_format", help="The format of renamed files. Default is '$artist/$album/$track $title.$extension'", default="$artist/$album/$track $title.$extension")
#parser.add_option("-c", "--check", dest="check", help="check files without moving them", metavar="FILE")

(options, args) = parser.parse_args()

verbose = options.verbose

if len(args) < 2:
    parser.error("incorrect number of arguments")

src_dirs = args[0:-1]
output_dir= args[-1].rstrip('/')

from string import Template

output_template = Template('%s/%s' % (output_dir,options.output_format))

# frames that won't be deleted in ID3v2Tag all others frames will be removed
mp3_good_frames = ['TPE1', 'TALB', 'TRCK', 'TIT2', 'TDRC', 'TCON']
minimal_frames = ['TPE1', 'TALB', 'TRCK', 'TIT2']

supported_formats=('mp3','flac','ogg','oga')

def handle_mp3(filename,write=False):
    try:
        audio = ID3(filename)
            
        # remove bad frames
        if write :
            for key in audio.keys():
                if key not in mp3_good_frames:
                    del audio[key]
            # convert tags to ID3v2.4 deleting ID3v1 tags
            audio.save(v1=0)
        
        if audio.has_key(minimal_frames[0]) and audio.has_key(minimal_frames[1]) and audio.has_key(minimal_frames[2]) and audio.has_key(minimal_frames[3]):
            track = audio['TRCK'].__str__()
            if '/' in track:
                track = track.split('/')[0]
        
            metadata = {
              'artist':audio['TPE1'].__str__(),
              'album':audio['TALB'].__str__(),
              'track':track,
              'title':audio['TIT2'].__str__().replace("/"," "),
              'extension':'mp3'
            }
            return metadata
      
        else:
            if verbose:
                print "file missing metadata", filename
            return False
    
    except ID3NoHeaderError :
        return False

def handle_ogg(filename, extension):
    audio = OggVorbis(filename)
    metadata = {
      'artist':audio['artist'][0],
      'album':audio['album'][0],
      'track':audio['tracknumber'][0],
      'title':audio['title'][0].replace("/"," "),
      'extension':extension
    }
    return metadata
  
def handle_flac(filename):
    audio = FLAC(filename)
    metadata = {
      'artist':audio['artist'][0],
      'album':audio['album'][0],
      'track':audio['tracknumber'][0],
      'title':audio['title'][0].replace("/"," "),
      'extension':'flac'
    }
    return metadata

def handle_file(filename,write=False):
    extension=filename.rsplit('.',1)[1]
    metadata = False
    if extension == 'mp3':
        metadata = handle_mp3(filename,write)
    elif extension == 'ogg' or extension == 'oga':
        metadata = handle_ogg(filename, extension)
    elif extension == 'flac':
        metadata = handle_flac(filename)
    return metadata

def handle_musicfiles(musicfiles, artist=None):
    for musicfile in musicfiles:
        #print musicfile[0], "%s/%s" % (output,output_format % (musicfile[1]))

        if artist:
            musicfile[1]['artist'] = artist

        dest_name = output_template.substitute(musicfile[1])
        src_name = musicfile[0]
        
        if verbose:
            print src_name,'\t', dest_name

        if options.move or options.copy:
            if not isdir(dirname(dest_name)):
                makedirs(dirname(dest_name))
        if options.move:
            move(src_name,dest_name)

        elif options.copy:
            copy(src_name,dest_name)
        
        if options.write :
            if options.move or options.copy:
                handle_file(dest_name,True)
            else:
                handle_file(src_name,True)
    
    #if delete empty folder that contains only jpg m3u txt or nfo files
    if options.move and options.delsrcdir:
        srcdir = dirname(src_name)
        for f in listdir(srcdir):
            if f[-3:] in ('nfo','m3u','nfo','jpg','txt'):
                tmpfile = join(srcdir,f)
                print "deleting file %s" % join(srcdir,f)
                remove(tmpfile)
        if len(listdir(srcdir)) == 0:
            rmdir(srcdir)
            if verbose:
                print "deleting empty folder",srcdir

def treat_dir(pathname):
    """
      treat recursively a folder
    """
    
    for root, dirs, files in walk(pathname):

        # for every dir or subdir
        artists=Set()
        musicfiles = []

        for item in files:
            tmp = item.rsplit('.',1)
            if len(tmp) == 2 and tmp[1] in supported_formats:
                item_name = join(root, item)
                metadata = False
                metadata = handle_file(item_name,options.write and not options.copy)
                if metadata == False:
                    print "file missing metadata", item_name
                else:
                    musicfiles.append([item_name,metadata])
                    artists.add(metadata['artist'])
    
        # is the artist unique for the folder ?
        if len(artists) == 1:
            handle_musicfiles(musicfiles,None)

        elif len(artists) > 1:
            # if it is a multiple artist album
            # for instance a soundtrack
            handle_musicfiles(musicfiles,"Compilation")
    
    # we delete the origin folder in case the -d option has been passed
    if options.move and options.delsrcdir:
        if isdir(pathname) and len(listdir(pathname)) == 0:
            if verbose:
                print "deleting empty origin folder",pathname
            rmdir(pathname)

if __name__ == "__main__":
    for src_dir in src_dirs:
        treat_dir(src_dir.rstrip('/'))

