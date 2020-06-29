+++
title = "Helloworld série : faire une fenêtre helloworld en Python et Gtk"
slug="Helloworld-serie-1-:-Python-et-Gtk"
draft = false
date = 2007-05-26
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "gtk","helloworld","python" ]
+++
J'entame une série de billet avec pour thème la comparaison de différents langages de programmation moderne et de différentes bibliothèques graphiques.
J'ai choisi de faire simple et, pour être un tant soit peu comparable, j'ai choisi de créer une fenêtre helloworld standard dans chacune des paires langage/librairie graphique. Juste une fenêtre et un bouton qui ferme la fenêtre.
Le but étant de faire découvrir les B-A-Ba de la programmation d'une interface graphique avec les différentes approches à la fois des langages et des librairies.
Au menu :
* les langages python,java,c++
* les librairies graphiques qt,gtk et swing.
Je ferais des billets python/gtk, python/qt, java/swing, c++/qt, au moins, et certainement c++/gtk.
Le premier de la série Helloworld est en python/Gtk.


La capture d'écran.
<img src="/py_gtk.png" alt="helloworld py/gtk" />
Attention elle a été faire sous kubuntu/KDE, elle n'aurait pas la même décoration et apparence sous ubuntu/GNOME.
Le source :
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pygtk # on importe les librairies grâce au module pygtk qui permet la communication entre python et gtk (qui est écrit dans un autre langage)
import gtk

class HelloWorld(gtk.Window): # remarquer la syntax python pour hériter d'une super-classe, ici gtk.Window qui est la classe de base des fenêtres en gtk
	def __init__(self):
		self = gtk.Window(gtk.WINDOW_TOPLEVEL) # appelle du constructeur de la super-classe
		self.set_title("Hello World !") # On choisit le titre de la fanêtre
		button = gtk.Button("Hello World !") # création d'un bouton
		button.connect("clicked", gtk.main_quit ) # connection de l'évènement du bouton clicked avec la fonction gtk.main_quit
		self.add( button) # on ajoute le bouton à la fenêtre
		self.connect("delete_event", gtk.main_quit ) # on "connecte" l'évènement de la fenêtre avec la même fonction
		self.show_all() # on affiche les composants
	def main(self):
		gtk.main()                 # pour pouvoir afficher des composants Gtk il est nécessaire de lancer cette fonction

if __name__ =="__main__": # équivalent du 'main' de java et c++
	hello = HelloWorld() # on  crée instance de l'objet HelloWorld - noter le typage dynamique de python
	hello.main() # lancement de l'interface
```

Plus aller plus loin, je vous recommande ces tutoriels :
* le[ tutoriel python en anglais](http://docs.python.org/tut/tut.html) de Guido Von Rossum (l'auteur de de python)
* [celui en français](http://www.cifen.ulg.ac.be/inforef/swi/python.htm) de Gérard Swinnen
* [le tutoriel en anglais](http://pygtk.org/pygtk2tutorial/index.html) sur python/Gtk