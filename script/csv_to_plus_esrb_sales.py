# -*- coding: utf-8 -*-
import csv
import re
with open("../data/CSV/vgsales-12-4-2019.csv","r",encoding="utf-8") as table, open("../data/CSV/plus_esrb_sales.csv","a",encoding="utf-8") as out:
    file=csv.reader(table,delimiter=",")
    fileOut=csv.writer(out,delimiter=",",lineterminator="\n")
    for line in file:
        rank,name,basename,genre = line[0:4]
        esrb = line[4]
        platform,publisher,developer = line[5:8]
        globalsa,usa,euro,jap = line[12:16]
        year = line[17]
        if year !="":
            year = re.sub(r"\.0$",r"",year)
        inter = [rank,name,basename,genre,esrb,platform,publisher,developer,globalsa,usa,euro,jap,year]
        if "" not in inter:
            fileOut.writerow(inter)
        continue