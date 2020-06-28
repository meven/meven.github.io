+++
title = "Test de OpenBSD l'OS le plus sur au monde"
slug="Test-de-OpenBSD-lOS-le-plus-sur-au-monde"
draft = false
date = 2007-06-09
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "BSD" ]
+++
J'ai installé OpenBSD et le moins que je puisse dire c'est que je n'ai pas été déçu !
<img src="/puffy41.gif" alt="Puffy la mas" />
[OpenBSD](http://fr.wikipedia.org/wiki/OpenBSD) est pour ce qui le savent pas un système Unix libre.
Historiquement il est basé sur le noyau [BSD](http://fr.wikipedia.org/wiki/Berkeley_Software_Distribution) lui-même héritié direct du noyau UNIX originel de 1970. C'est donc un cousin éloigné du noyau Linux.
Voilà pour la petite histoire.

OpenBSD est dans la famille des [*BSD](http://fr.wikipedia.org/wiki/BSD), le plus orienté sécurité. Le système est réputé pour cela. On lui doit notamment [openSSH](http://fr.wikipedia.org/wiki/OpenSSH), l'implémentation libre du célèbre protocole ssh.

Le système est à des années lumières de la simplicité de ubuntu qu'on se le dise mais il n'est fait pour. Ce qu'il recherche c'est la sécurité maximum et la fiabilité.
Résultat une installation en mode texte( partitionage ..), pas d'interface graphique installée par défaut. Pas de compte sudo non plus, un compte root après à toi de te débrouillé. La seule chose en commun avec linux, c'est le shell ! Et encore ici pas de bash c'est ksh ou csh !

Pas de système de gestion de packet style apt (debian/ubuntu) ou emerge(gentoo). Pour installer un logiciel, il faut d'abord ajouter dans une variable d'environnement l'emplacement du serveur ftp qui fait office de dépôt. On utilise alors le script pkg_add. Il télécharge les packets au format tgz (tar.gz) contenant les binaires et le reste. Le script gère les dépendances. J'ai pu installé Kde mais ce n'est pas parfait. La résolution a un problème, il n'y a ni konqueror ni les autres application utiles et je ne peux lancer KDE que avec l'utilisateur root.

Un conseil si vous voulez l'essayer, renseignez vous bien surtout si vous voulez tenter un dual boot. Personnellement je ne l'aurais pas essayer si je n'avais pas un disque dur de libre.
[Site officiel](http://www.openbsd.org/)
[Side de la communauté française](http://www.openbsd-france.org/[fr)