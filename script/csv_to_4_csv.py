# -*- coding: utf-8 -*-
import csv
import re

#ouverture du fichier d'entrée et des 4 fichiers de sortie
with open("../data/CSV/vgsales-12-4-2019.csv","r",encoding="utf-8") as table, open("../data/CSV/basic.csv","a",encoding="utf-8") as out1, open("../data/CSV/plus_sales.csv","a",encoding="utf-8") as out2, open("../data/CSV/plus_critic_sales.csv","a",encoding="utf-8") as out3, open("../data/CSV/plus_esrb_sales.csv","a",encoding="utf-8") as out4:
    
	#on instancie le reader et le writer du module CSV pour gérer proprement la lecture et l'écriture
    file = csv.reader(table,delimiter=",")
    fileOut1 = csv.writer(out1,delimiter=",",lineterminator="\n")
    fileOut2 = csv.writer(out2,delimiter=",",lineterminator="\n")
    fileOut3 = csv.writer(out3,delimiter=",",lineterminator="\n")
    fileOut4 = csv.writer(out4,delimiter=",",lineterminator="\n")
    
	#pour chaque ligne du fichier initial
	#on va garder les informations qui nous intéressent et les stocker dans des variables
    for line in file:
        rank,name,basename,genre = line[0:4]
        platform,publisher,developer = line[5:8]
        year = line[17]
        globalsa,usa,euro,jap = line[12:16]
        critic = line[9]
        esrb = line[4]
        
		#on vérifie que l'année ne soit pas vide
		#si non vide, alors on nettoie son format
        if year != "":
            year = re.sub(r"\.0$",r"",year)
			#on fait des listes intermédiaires pour chaque fichier selon les champs que l'on garde par fichier
            inter1 = [rank,name,basename,genre,platform,publisher,developer,year]
            inter2 = [rank,name,basename,genre,platform,publisher,developer,year,globalsa,usa,euro,jap]
            inter3 = [rank,name,basename,genre,platform,publisher,developer,year,globalsa,usa,euro,jap,critic]
            inter4 = [rank,name,basename,genre,platform,publisher,developer,year,globalsa,usa,euro,jap,esrb]
			#si tous les champs contiennent une valeur, alors on écrit la ligne dans le bon fichier
			#si un des champs est vide, alors on n'écrit pas la ligne dans le fichier qui lui correspond
            if "" not in inter1:
                fileOut1.writerow(inter1)
            if "" not in inter2:
                fileOut2.writerow(inter2)
            if "" not in inter3:
                fileOut3.writerow(inter3)
            if "" not in inter4:
                fileOut4.writerow(inter4)
            continue
    print('CSV file "basic.csv" generated ! \n')
    print("------------------------------")
    print('CSV file "plus_sales.csv" generated ! \n')
    print("------------------------------")
    print('CSV file "plus_critic_sales.csv" generated ! \n')
    print("------------------------------")
    print('CSV file "plus_esrb_sales.csv" generated ! \n')
    print("------------------------------")