from empleados import empleado
from datetime import date
from datetime import datetime
class empcontratado(empleado):
    __fechainicio = date
    __fechafinalizacion = date
    __canthoras = 0
    __valorhora = 1000

    def __init__(self,dni,nom,dire,tel,fechaini,fechafin,cant):
        super().__init__(dni, nom, dire, tel)
        self.__fechainicio = datetime.strptime(fechaini, '%d/%m/%Y')
        self.__fechafinalizacion = datetime.strptime(fechafin, '%d/%m/%Y')
        self.__canthoras = cant


    def horas(self):
     return  self.__canthoras
    def gethora(self,can):
        self.__canthoras = can
    def valhora(self):
     return self.__valorhora
    def sueldo(self):
        return int(self.__canthoras) * int(self.__valorhora)
    def setsueldo(self,monto):
        print('valor por hora: '+ str(self.__valorhora))
        self.__valorhora = monto

    def tipo(self):
        return 'empleado contratado'

