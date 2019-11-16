# -*- coding: utf-8 -*-
import csv
import re
with open("../data/CSV/vgsales-12-4-2019.csv","r",encoding="utf-8") as table, open("../data/CSV/basic.csv","a",encoding="utf-8") as out1, open("../data/CSV/plus_sales.csv","a",encoding="utf-8") as out2, open("../data/CSV/plus_critic_sales.csv","a",encoding="utf-8") as out3, open("../data/CSV/plus_esrb_sales.csv","a",encoding="utf-8") as out4:
    
    file=csv.reader(table,delimiter=",")
    fileOut1=csv.writer(out1,delimiter=",",lineterminator="\n")
    fileOut2=csv.writer(out2,delimiter=",",lineterminator="\n")
    fileOut3=csv.writer(out3,delimiter=",",lineterminator="\n")
    fileOut4=csv.writer(out4,delimiter=",",lineterminator="\n")
    
    for line in file:
        rank,name,basename,genre = line[0:4]
        platform,publisher,developer = line[5:8]
        year = line[17]
        globalsa,usa,euro,jap = line[12:16]
        critic = line[9]
        esrb = line[4]
        
        if year != "":
            year = re.sub(r"\.0$",r"",year)
            inter1 = [rank,name,basename,genre,platform,publisher,developer,year]
            inter2 = [rank,name,basename,genre,platform,publisher,developer,year,globalsa,usa,euro,jap]
            inter3 = [rank,name,basename,genre,platform,publisher,developer,year,globalsa,usa,euro,jap,critic]
            inter4 = [rank,name,basename,genre,platform,publisher,developer,year,globalsa,usa,euro,jap,esrb]
            if "" not in inter1:
                fileOut1.writerow(inter1)
            if "" not in inter2:
                fileOut2.writerow(inter2)
            if "" not in inter3:
                fileOut3.writerow(inter3)
            if "" not in inter4:
                fileOut4.writerow(inter4)
            continue
            
    
    
    
    
    
         
       
       
  
        
        
    