+++
title = "Google Wave s'ouvre un peu"
slug="Google-Wave-s-ouvre-un-peu"
draft = false
date = 2009-07-25
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "développement web","internet","wave" ]
+++
Google a fait [l'annonce](http://googlewavedev.blogspot.com/2009/07/google-wave-federation-protocol-and.html) d'une libération de code sous Licence Apache 2, de deux programmes en relation avec le protocole Wave.
Cela représente au total 40 000 lignes de code de java disponible via [mercurial](http://fr.wikipedia.org/wiki/Mercurial).

# le "Operational Transform" (OT), c'est en fait l'API de base pour le protocole Wave et son modèle.
# un prototype de client/serveur implémentant le protocole Wave.

Le serveur est une extension du serveur XMPP [openfire](http://www.igniterealtime.org/projects/openfire/index.jsp).
Une procédure d'installation est disponible, que j'ai testé.

<a href="/captures/wave/Capture-Wave-console.png" title=""><img src="/captures/wave/Capture-Wave-console.png" /></a>

On se retrouve avec un serveur XMPP avec l'extension Wave et un client en ligne de commande avec des commandes tel que :

  /open     id                       open a wave given an inbox id

On retrouve les principes des waves : partage d'objet, mise à jour temps réel entre les participants.

Le client n'a pas encore qu'une fraction des fonctionnalités du client GWT, mais avec une base de code pour travailler, qui sait ce que l'on peut obtenir.

Pour le serveur, d'après le billet de google, il implémente une version plus récente du protocole que le serveur de preview wavesandbox...