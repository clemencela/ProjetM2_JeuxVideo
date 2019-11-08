# -*- coding: utf-8 -*-
import csv
import re
with open("../data/CSV/vgsales-12-4-2019.csv","r",encoding="utf-8") as table, open("../data/CSV/basic.csv","a",encoding="utf-8") as out:
    file=csv.reader(table,delimiter=",")
    fileOut=csv.writer(out,delimiter=",",lineterminator="\n")
    #on ne prend pas la colonne 4: ESRB_Rating
    #de 8 à 16 inclus, on ne prend pas
    #de 18 à 22 inclus, pareil
    for line in file:
        rank,name,basename,genre = line[0:4]
        platform,publisher,developer = line[5:8]
        year = line[17]
        if year != "":
            year = re.sub(r"\.0$",r"",year)
            fileOut.writerow([rank,name,basename,genre,platform,publisher,developer,year])
        continue
    
        