from empleados import  empleado
class empplanta(empleado):
    __sueldobasico = 0
    __antiguedad = 0

    def __init__(self,dni,nom,dire,tel,suel,anti):
        super().__init__(dni, nom, dire, tel)
        self.__sueldobasico = suel
        self.__antiguedad = anti

    def sueldobasico(self):
     return self.__sueldobasico
    def antiguedad(self):
        return  self.__antiguedad
    def sueldo(self):
        return int(self.__sueldobasico) + ((1*int(self.__sueldobasico)/100) * int(self.__antiguedad))

    def setsueldo(self,monto):
        print('valor basico acutal: '+ str(self.__sueldobasico))
        self.__sueldobasico = monto
    def tipo(self):
        return 'empleado planta'