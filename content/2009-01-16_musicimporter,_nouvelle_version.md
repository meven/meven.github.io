+++
title = "musicimporter, nouvelle version"
slug="musicimporter-nouvelle-version"
draft = false
date = 2009-01-16
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "musicimporter","python","script" ]
+++
Voici une nouvelle version de mon script [musicimporter](/post/2008/09/07/MusiImporter-importer-proprement-ses-fichiers-audio-dans-sa-collection) qui permet de déplacer, renommer et nettoyer des fichiers musicaux. Par nettoyer, j'entends supprimer les tags inutiles dans les fichiers mp3 (commentaires,...).

Le script permet désormais également de supprimer les dossiers qui contenaient les fichiers musicaux lorsqu'ils sont devenus inutiles pour encore davantage automatiser l'import de fichier de musique.

#### Les nouveautés
* supporte les fichiers ogg avec l'extension oga
* nouvelle option -d, supprime les fichiers inutiles dans le dossier source (fichier txt jpg m3u et nfo) et les dossiers sources qui sont devenus vides suite à l'exécution du script. À utiliser conjointement avec l'option -m.
* nouvelle option -c, pour copier les fichiers au lieu de les déplacer, modifie les tags après le déplacement.
* amélioration générale du code, plusieurs bugs corrigés

#### Exemple d'utilisation

On vérifie que l'import est possible (le script indiquera si il manque des tags aux fichiers par exemple):

```
musicimporter -v Dossier Source/ ~/Musique/
```

Si tout c'est bien passé, on importe dans sa collection :

```
musicimporter -vmwd Dossier Source/ ~/Musique/
```

La prochaine fonctionnalité envisagée est de permettre l'utilisation d'un fichier de configuration plutôt que des options en ligne de commande.

__Téléchargement : [musicimporter.py](http://www.bivouak.fr/public/musicimporter.py).__

Tous les commentaires sont les bienvenus.