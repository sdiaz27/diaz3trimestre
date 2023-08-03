class Paises:
    def __init__(self,pais,pobla,superf,altura):
        self.__pais=pais
        self.__pobla=pobla
        self.__superf=superf
        self.__altura=altura
    def info(self):
        return f"{self.__pais} {self.__pobla} {self.__superf} {self.__altura}"
    
    def getPais(self):
        return self.__pais
    
    def getPobla(self):
        return self.__pobla
    
    def getSuperf(self):
        return self.__superf
    
    def getAltura(self):
        return self.__altura