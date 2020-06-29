+++
title = "MusicImporter, importer proprement ses fichiers audio dans sa collection."
slug="MusiImporter-importer-proprement-ses-fichiers-audio-dans-sa-collection"
draft = false
date = 2008-09-07
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "musicimporter","python","script" ]
+++
Je viens d'écrire un script en python pour se simplifier la vie dans le classement/rangement de fichier audio récupéré.
Il s'appelle simplement musicimporter.


#### Utilisation

Le script prend en entrée un nombre quelconque de dossiers et un dossier de sortie.
Il cherche récursivement les fichiers se trouvant dans les sous répertoires des dossiers en entrée. Il traite ensuite les dossiers trouvés selon les options sélectionnées.
Pour l'instant, seuls les formats ogg vorbis, flac et mp3 sont supportés.


* L'option -w nettoie les tags des fichiers mp3 trouvés, en supprimant tous les tags ne concernant pas le titre, l'album, l'année ou le numéro de la chanson. L'option convertit également le tags ID3v1 subsistant en tag ID3v2.4.
* L'option -m déplace les fichiers dans le dossier output_dir suivant le format de sortie. Le format peut être changer avec l'option -o.
* -v, verbose mode, permet de suivre de plus prêt ce que fait le script.

```
Usage: musicimporter.py [options] src_dir... output_dir

moves and renames audio files cleaning files metadata. It supports mp3 Ogg
Vorbis and Flac

Options:
  -h, --help            show this help message and exit
  -v, --verbose
  -w, --write           clean metadata of mp3 files, delete ID3v1 tags in
                        favor of ID3v2.4
  -m, --move            move files
  -o OUTPUT_FORMAT, --output-format=OUTPUT_FORMAT
                        The format of renamed files. Default is
                        '$artist/$album/$track $title.$extension'
```
Ce script nécessite [mutagen](http://www.sacredchao.net/quodlibet/wiki/Development/Mutagen).
Disponible dans Debian/ubuntu dans le paquet python-mutagen .

Téléchargement : [musicimporter.py](http://www.bivouak.fr/public/musicimporter.py).

Si vous avez des remarques ou suggestions laissez un commentaire.