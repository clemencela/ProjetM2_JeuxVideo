# -*- coding: utf-8 -*-
from pathlib import Path
import csv
from lxml import etree

def basic(row):
	"""Prend en entrée une ligne de CSV sous forme de liste et crée les différents éléments
	de la modélisation XML pour les informations basiques"""
	
	#on  définit la variable game comme global pour qu'elle soit
	#accessible par les autres fonctions
    global game
	
	#élément game inclus dans la racine
	#un attribut rank qui vient du champ "rank"
    game = etree.SubElement(root,"game")
    game.set("rank",row[0])
    
	#élément name inclus dans game
	#éléments official et ascii inclus dans name : valeurs des champs "Name" et "basename"
    name = etree.SubElement(game,"name")
    official = etree.SubElement(name,"official")
    official.text = row[1]
    infoascii = etree.SubElement(name,"ascii")
    infoascii.text = row[2]
    
	#élément genre inclus game
	#valeur du champ "Genre"
    genre = etree.SubElement(game,"genre")
    genre.text = row[3]
    
	#élément platform inclus dans game
	#valeur du champ "Platform"
    platform = etree.SubElement(game,"platform")
    platform.text = row[4]
    
	#élément production inclus dans game
	#éléments publisher et developer inclus dans production : valeurs des champs "Publisher" et "Developer"
    production = etree.SubElement(game,"production")
    publisher = etree.SubElement(production,"publisher")
    publisher.text = row[5]
    developer = etree.SubElement(production,"developer")
    developer.text = row[6]
    
	#élément year inclus dans game
	#valeur du champ "Year"
    year = etree.SubElement(game,"year")
    year.text = row[7]
    
def sales(row):
	"""Prend en entrée une ligne de CSV sous forme de liste et crée les différents éléments
	de la modélisation XML pour les informations de ventes"""
	
	#élément distribution inclus dans game
    distribution = etree.SubElement(game,"distribution")
	
	#élément sales inclus dans distribution
	#son attribut area aura comme valeur "global" et contenu de l'élément = champ "Global_Sales"
    sales1 = etree.SubElement(distribution,"sales")
    sales1.set("area","global")
    sales1.text = row[8]
    
	#élément sales inclus dans distribution
	#son attribut area aura comme valeur "usa" et contenu de l'élément = champ "NA_Sales"
    sales2 = etree.SubElement(distribution,"sales")
    sales2.set("area","usa")
    sales2.text = row[9]
    
	#élément sales inclus dans distribution
	#son attribut area aura comme valeur "europe" et contenu de l'élément = champ "PAL_Sales"
    sales3 = etree.SubElement(distribution,"sales")
    sales3.set("area","europe")
    sales3.text = row[10]
    
	#élément sales inclus dans distribution
	#son attribut area aura comme valeur "japan" et contenu de l'élément = champ "JP_Sales"
    sales4 = etree.SubElement(distribution,"sales")
    sales4.set("area","japan")
    sales4.text = row[11]
    
def critic(row):
	"""Prend en entrée une ligne de CSV sous forme de liste et crée l'élément
	de la modélisation XML pour la note du jeu obtenue par la critique"""
	
	#élément critic_score inclus dans game
	#valeur du champ "Critic_Score"
    critic = etree.SubElement(game,"critic_score")
    critic.text = row[12]

def esrb(row):
	"""Prend en entrée une ligne de CSV sous forme de liste et crée l'élément
	de la modélisation XML pour le symbole ESRB du jeu"""
	
	#élément esrb_rating inclus dans game
	#valeur du champ "ESRB_Rating"
    esrb = etree.SubElement(game,"esrb_rating")
    esrb.text = row[12]

#répertoire contenant les fichiers CSV	
directory = Path("../data/CSV")

#répertoire de sortie qui contiendra les fichiers XML
outDir = Path("../xml")

#itération dans le répertoire des CSV pour lire chaque jeu de données avec le reader CSV
#on vérifie qu'on ait bien un fichier
#et qu'il ne s'agit pas du jeu de données CSV d'origine ("vgsales-12-4-2019.csv")
for child in directory.iterdir():
    if child.is_file():
        if child.match("vgsales*"):
            continue
        with open(child,"r",encoding="utf-8") as file:
            
            print(f'Reading "{child.name}" to generate an XML document...\n')
			
			#on initialise une variable qui contiendra une lettre pour savoir quel jeu de données on a
            nameF = ""
			
			#on récupére le nom du fichier sans l'extension et on ajoute l'extension ".xml"
			#pour avoir le nom de fichier de sortie
            nameOut = child.stem + ".xml"
			
			#on crée le chemin pour accéder à ce fichier de sortie
            pathToF = outDir.joinpath(nameOut)
            
			#objet reader pour lire proprement le fichier
            table = csv.reader(file,delimiter = ",")
			
			#on passe une ligne, celle des en-têtes
            next(table)
            
			#racine collection de chaque fichier XML
            root = etree.Element("collection")
			
			#on va parcourir les lignes du jeu de données
			#pour agrandir l'arborescence XML (etree) au fur et à mesure pour chaque modélisation
			#on fait des tests pour vérifier quel jeu de données on a et on donne une lettre à notre variable de nom
			#on appelle ensuite les bonnes fonctions sur la ligne pour agrandir notre arbre
            for row in table:
                if child.match("basic.csv"):
                    nameF = "B"
                    basic(row)
                if child.match("plus_sales.csv"):
                    nameF = "S"
                    basic(row)
                    sales(row)
                if child.match("plus_critic*.csv"):
                    nameF = "C"
                    basic(row)
                    sales(row)
                    critic(row)
                if child.match("plus_esrb*.csv"):
                    nameF = "E"
                    basic(row)
                    sales(row)
                    esrb(row)
			
			#quand une lecture de jeu de données est finie
			#on fait des tests pour savoir quel jeu de données on a
			#on récupère l'arbre XML que les fonctions ont agrandi au fur et à mesure
			#et on l'écrit dans le fichier correspondant
			#en ajoutant une déclaration XML ainsi qu'une indention
            if nameF == "B":
                tree = etree.ElementTree(root)
                tree.write(str(pathToF), encoding="utf-8",xml_declaration=True, method="xml",pretty_print=True)
                print(f'XML document "{nameOut}" generated ! \n')
                print("------------------------------")
                
            if nameF == "S":
                tree = etree.ElementTree(root)
                tree.write(str(pathToF), encoding="utf-8",xml_declaration=True, method="xml",pretty_print=True)
                print(f'XML document "{nameOut}" generated ! \n')
                print("------------------------------")
                
            if nameF == "C":
                tree = etree.ElementTree(root)
                tree.write(str(pathToF), encoding="utf-8",xml_declaration=True, method="xml",pretty_print=True)
                print(f'XML document "{nameOut}" generated ! \n')
                print("------------------------------")
            
            if nameF == "E":
                tree = etree.ElementTree(root)
                tree.write(str(pathToF), encoding="utf-8",xml_declaration=True, method="xml",pretty_print=True)
                print(f'XML document "{nameOut}" generated ! \n')
                print("------------------------------")