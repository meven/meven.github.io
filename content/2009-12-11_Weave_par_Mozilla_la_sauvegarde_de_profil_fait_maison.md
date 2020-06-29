+++
title = "Weave par Mozilla la sauvegarde de profil fait maison"
slug="Weave-par-Mozilla-la-sauvegarde-de-profil-fait-maison"
draft = false
date = 2009-12-11
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "extension","mozilla","web" ]
+++
Avec la sortie des extensions dans google chrome et la version 4, il me vient une idée :
Et si pour synchroniser mes marques-pages je pouvais me passer des serveurs de google pour changer.
Et mieux encore, et si, je pouvais synchroniser les deux meilleurs navigateurs du moment chrome et firefox.

J'en rếvais, Mozilla l'a déjà fait.
Le projet dont je parle s'appelle [Weave](https://mozillalabs.com/weave/).
Il est issu du Mozilla Labs, la pépinière d'innovation de mozilla.
<img src="/logos/weave-logo.png" alt="Mozilla Weave" />
Il vise à permettre de fusionner ses marques-pages d'un poste à l'autre et plus encore, de manière sécurisée et {{in the cloud}} --(Un buzzword, un)--.


D'un côté une extension firefox ou fennec (le firefox mobile) qui récupère les données et de l'autre un serveur qui les stockent et les rend disponible n'importe quand.


Ce type de fonctionnalités n'est pas nouveau, et google le propose dans chrome directement sans extensions.
La grande différence avec les autres services du genre et celui de google est selon moi __son ouverture__.
Le code est entièrement ouvert côté client (l'extension pour firefox) et, chose moins commune, [côté serveur](https://wiki.mozilla.org/Labs/Weave/1.0/Setup/Storage).


Résultat : rien n'empêche d'héberger son propre serveur weave pour plus d'indépendance vis à vis de google ou même de mozilla. 
C'est ce que j'ai fait grâce à la [procédure](https://wiki.mozilla.org/Labs/Weave/1.0/Setup/Storage) du wiki de weave (attention la documentation a des défauts, à suivre avec précaution). Le serveur est en Php, ce qui simplifie grandement le déploiement.

<a href="/captures/Capture.png" title=""><img src="/captures/Capture.png" /></a>

L'outil est d'ores et déjà fonctionnel et la version 1.0 est en préparation.

Dans ces conditions, à quand une synchronisation des marques-pages et paramètres de chrome avec weave et mieux encore avec firefox. Le tout totalement __indépendamment de google !__

Je pense que ce n'est qu'une question de temps, sinon je m'intéresserais bien à l'écriture d'une extension pour chrome ;).