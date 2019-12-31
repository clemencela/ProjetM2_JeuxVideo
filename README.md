# ProjetM2_JeuxVideo
Contenu du projet dans le cadre du cours "Documents structurés"

## Objectifs du projet
Faire des classements de jeux vidéo en fonction des ventes et de leur genre, leur plateforme, leurs différentes notes, leur date de sortie et les pays consommateurs etc.

## Source des données

https://www.kaggle.com/ashaheedq/video-games-sales-2019/version/2

## Gestion du projet

La gestion de notre projet s'est fait sur cette page : https://github.com/users/clemencela/projects/1

## Description de l'architecture

Ci-dessous la description de chaque répertoire et ce qu'il contient

### data

Contient un répertoire CSV contenant le fichier d'origine du corpus : 
```
vgsales-12-4-2019.csv
```

Ainsi que les 4 csv générés pour notre projet : 
```
basic.csv
plus_critic_sales.csv
plus_esrb_sales.csv
plus_sales.csv
```

### grammaire

Contient les 3 grammaires de validation pour nos documents XML : 
```
DTD.dtd
relax_compact_pour_4.rnc
relax_patron_pour_4.rng
```

### graphs

Contient 4 sous-répertoires dans lesquels sont stockés les graphiques avant leur insertion dans les pages web

### notes

Contient 2 fichiers texte contenant des prises de notes réalisées au début du projet

### requetes

Contient 4 sous-répertoires dans lesquels sont stockées les requêtes XQuery et leur résultat

### requetes_arrays

Contient 4 sous-répertoires dans lesquels sont stockés les fichiers texte contenant les résultats formattés en Google arrays

### script

Contient les 3 scripts écrits pour le projet : 
```
csv_to_4_csv.py
csv_to_xml.py
transfo_result_google_array.py
```

### transformation

Contient la feuille de style XSLT permettant de transformer la page demarche.xml (dans le répertoire "web") en page html bien formatté selon le style du site

### web

Contient tout le site web avec ses différentes pages, images, documents etc.

### xml

Contient les 4 fichiers XML générés pour le projet :
```
basic.xml
plus_critic_sales.xml
plus_esrb_sales.xml
plus_sales.xml
```

## A noter

Dans le répertoire "notes", vous trouverez des informations notées au fur et à mesure de l'avancement du projet...dont les futures statistiques que nous voudrions présenter sur notre site final :smiley:

Le fichier "membres.txt" contient les noms de deux étudiantes composant le groupe de travail.