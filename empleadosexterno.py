import datetime
from datetime import datetime
from empleados import empleado
from datetime import date
class empexterno(empleado):
    __tarea = ''
    __fechainicio = date
    __fechafinaliza = date
    __montoviatico = 0
    __costoobra = 0
    __montosegurovida = 0

    def __init__(self,dni,nom,dire,tel,tare,fechaini,fechafin,montovia,cosobr,mont):
        super().__init__(dni,nom,dire,tel)
        self.__tarea = tare
        self.__fechainicio = datetime.strptime(fechaini, '%d/%m/%Y')
        self.__fechafinaliza = datetime.strptime(fechafin, '%d/%m/%Y')
        self.__montoviatico = montovia
        self.__costoobra = cosobr
        self.__montosegurovida = mont

    def tarea(self):
        return self.__tarea
    def costoobra(self):
        return self.__costoobra
    def fecha(self):
        return self.__fechafinaliza
    def viatico(self):
        return self.__montoviatico
    def montoseguro(self):
        return self.__montosegurovida

    def sueldo(self):
       return  int(self.__costoobra) - int(self.__montosegurovida) - int(self.__montoviatico)
    def setsueldo(self,monto):
        print('valor monto viatico actual: '+ str(self.__montoviatico))
        self.__montoviatico = monto
    def tipo(self):
        return 'empleado externo'

