import abc
from abc import ABC
class empleado(ABC):
    __dni = 0
    __nombre = ''
    __direccion = ''
    __telefono = 0

    def __init__(self,dni,nom,dire,tel):
        self.__dni = dni
        self.__telefono = tel
        self.__telefono = dire
        self.__nombre = nom

    @abc.abstractmethod
    def sueldo(self):
     pass

    @abc.abstractmethod
    def setsueldo(self):
     pass
    @abc.abstractmethod
    def tipo(self):
        pass
    def dni(self):
     return self.__dni

    def clase(self):
     return type(self)
    def nombre(self):
        return self.__nombre
    def tele(self):
        return self.__telefono
    def lista(self):
        print(self.__nombre)
        print(self.__dni)
        print(self.__telefono)