
from Paises import *
import csv
listaPaises=[]
with open('archivo objet/pais.csv',encoding="utf-8") as csvDataFile:

    csvPais=csv.reader(csvDataFile)    
    for row in csvPais:
        ob=Paises(row[1],row[3],row[4],row[7])
        listaPaises.append(ob)
    
for pis in listaPaises:
 
    print('name pais:',pis.getPais())
    print('poblacion:',pis.getPobla())
    print('superficie:',pis.getSuperf())
    print('altura:',pis.getAltura())
    

    