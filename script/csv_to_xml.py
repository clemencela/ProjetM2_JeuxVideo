# -*- coding: utf-8 -*-
from pathlib import Path
import csv
from lxml import etree

def basic(row):
    global game
    game = etree.SubElement(root,"game")
    game.set("rank",row[0])
        
    name = etree.SubElement(game,"name")
    official = etree.SubElement(name,"official")
    official.text = row[1]
    infoascii = etree.SubElement(name,"ascii")
    infoascii.text = row[2]
        
    genre = etree.SubElement(game,"genre")
    genre.text = row[3]
    
    platform = etree.SubElement(game,"platform")
    platform.text = row[4]
    
    production = etree.SubElement(game,"production")
    publisher = etree.SubElement(production,"publisher")
    publisher.text = row[5]
    developer = etree.SubElement(production,"developer")
    developer.text = row[6]
        
    year = etree.SubElement(game,"year")
    year.text = row[7]
    
def sales(row):
    distribution = etree.SubElement(game,"distribution")
    sales1 = etree.SubElement(distribution,"sales")
    sales1.set("area","global")
    sales1.text = row[8]
    
    sales2 = etree.SubElement(distribution,"sales")
    sales2.set("area","usa")
    sales2.text = row[9]
    
    sales3 = etree.SubElement(distribution,"sales")
    sales3.set("area","europe")
    sales3.text = row[10]
    
    sales4 = etree.SubElement(distribution,"sales")
    sales4.set("area","japan")
    sales4.text = row[11]
    
def critic(row):
    critic = etree.SubElement(game,"critic_score")
    critic.text = row[12]

def esrb(row):
    esrb = etree.SubElement(game,"esrb_rating")
    esrb.text = row[12]

directory = Path("../data/CSV")
outDir = Path("../xml")
for child in directory.iterdir():
    if child.is_file():
        if child.match("vgsales*"):
            continue
        with open(child,"r",encoding="utf-8") as file:
            
            print(f'Reading "{child.name}" to generate an XML document...\n')
            nameF = ""
            nameOut = child.stem + ".xml"
            pathToF = outDir.joinpath(nameOut)
            
            table = csv.reader(file,delimiter = ",")
            next(table)
            
            root = etree.Element("collection")
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