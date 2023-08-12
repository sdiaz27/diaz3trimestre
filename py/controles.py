
def lineas(file):
    contar=0
    read_txt = open(file,'r')
    for i in read_txt.readlines():
        print(i)
        contar+=1
    if contar ==1:
        print(f'las cantidad de las lineas son {contar}')
    elif contar >1:
        print(f'las cantidad de las lineas son {contar}')
    else:
        print('No hay lineas')
    read_txt.close

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
    read_txt.close
    
lineas('C:\diaztercertrimestre\ejercicio.txt')
caracter('C:\diaztercertrimestre\ejercicio.txt')
