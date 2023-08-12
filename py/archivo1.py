#un programa donde cree una carpeta que guarde sus datos con un a funcion que guarde cuantos caracteres y linias tiene 

archi1=open("archivo.txt","w") 
archi1.write("sebastian diaz lache \n") 
archi1.write("CC1031800244\n") 
archi1.write("RHo+\n")  
archi1.close() 

archi1=open("archivo.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()

def caracter (file):
    contar=0
    read_txt = open(file,'r')
    for i in read_txt.read():
        contar+=1
    if contar ==1:
        print(f'las cantidad de caracteres son {contar}')
    elif contar >1:
        print(f'las cantidad de carracteres son {contar}')
    else:
        print('No hay caracteres')
    archi1.close()

def linea (file):
    contar=0
    read_txt = open(file,'r')
    for i in read_txt.readlines():
        contar+=1
    if contar ==1:
        print(f'las cantidad de lineas son {contar}')
    elif contar >1:
        print(f'las cantidad de lineas son {contar}')
    else:
        print('No hay lineas')
    archi1.close()

    
caracter('archivo.txt')
linea('archivo.txt')
