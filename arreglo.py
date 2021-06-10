import numpy
from numpy import  *
from empleados import empleado
class Arreglo:
    __dimension = 0
    __actual = 0
    __cuerpo = None
    def __init__(self,dimension):
        self.__cuerpo = numpy.empty(dimension, dtype=empleado)
        self.__dimension = dimension
        self.__cantidad = 0
    def agregar(self,unempleado):
     self.__cuerpo[self.__actual] = unempleado
     self.__actual+=1

    def dime(self):
     return self.__dimension
    def actual(self):
      return self.__actual


    def a(self,x):
        return self.__cuerpo[x]
