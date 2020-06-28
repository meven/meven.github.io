+++
title = "Fosdem 2009 troisième partie"
slug="Fosdem-2009-troisieme-partie"
draft = false
date = 2009-03-07
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "fosdem" ]
+++
#### [Upstart](http://upstart.ubuntu.com/) par Scott James Remnant

L'objectif de Upstart est de fournir un gestionnaire de démarrage remplaçant des scripts init et un système de gestion de services, leur démarrage, arrêt et status.

Les avancés promises par Upstart sont nombreuses.
On oublie les "sleep" dans les scripts init qui faisait perdre beaucoup de temps au démarrage.
Upstart sera charger de synchroniser le démarrage des services du sytème et d'en gérer les dépendances, Par exemple 'gnome a besoin de dbus pour démarrer.'.
Il fournit également un mécanisme d'évènements du type "dbus quitte".
Oublier la torture des runlevels.

Upstart est utilisé dans ubuntu et dans fedora 10.

L'année 2009 devrait être marquée par ce projet par la sortie de upstart 1.0 ou bien 0.5 si toutes les fonctionnalités ne sont pas implémentées.
Cette future version sera le fruit d'une réécriture complète.

#### [MediaWiki](http://fosdem.org/2009/schedule/events/mediawiki) par Brion Vibber ([CTO](http://en.wikipedia.org/wiki/Chief_technical_officer) de l'ONG Wikimedia)

[((http://farm1.static.flickr.com/197/3263794887_dcda6058c4_m.jpg|Conférence MediaWiki|C))|http://www.flickr.com/photos/philliecasablanca/3263794887/sizes/l/]
[Photo par Phillie Casablanca sous licence CC](http://www.flickr.com/photos/philliecasablanca/3263794887/)


> Vous connaissez sans doute wikipedia.
> Si vous ne le connaissez pas, c'est sans doute que vous n'avez pas été sur internet depuis un moment.
C'est une citation du conférencier que j'ai pu intercepter.

La fondation [wikimedia](http://fr.wikipedia.org/wiki/Wikimedia_Foundation) se fixe d'ambitieux objectifs.
La conférence parle du point de vue technique, on parle donc de mediawiki, le wiki qui fait vivre [wikipedia](http://fr.wikipedia.org/wiki/Accueil).

Apprendre de wordpress pour l'amélioration de l'utilisabilité/ergonomie, ouvrir le développement de mediawiki au maximum pour avoir une liaison avec la communauté (actuellement ce projet compte 55 développeurs et quelques millions d'utilisateur :P).