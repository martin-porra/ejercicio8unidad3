import numpy
from numpy import *
from zope.interface import implementer
from datetime import datetime
from  empleadoplanta import  empplanta
from  empleadosexterno import  empexterno
from  empleadocontratado import  empcontratado
import csv
from  numpy import *
from arreglo import Arreglo
from itesorero import ITesorero
from ingerente import IGerente

@implementer(ITesorero)
@implementer(IGerente)
class manejador:

    def __init__(self):
        dim = int(input('indicar tamaño de arreglo '))
        while dim < self.contar():
            print('Error: el numero debe ser mayor a la cantidad de empleados que hay en los archivos')
            dim = int(input('ingrese nuevamente el numero de componentes del arreglo '))
        self.arre = Arreglo(dim)
        self.añadir()

    def añadir(self):
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            objeto = empplanta(fila[0], fila[1], fila[2], fila[3], fila[4],fila[5])
            self.arre.agregar(objeto)
        archivo.close()
        archivo = open('contratados.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            objeto = empcontratado(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6])
            self.arre.agregar(objeto)
        archivo.close()
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            objeto = empexterno(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6],fila[7],fila[8],fila[9])
            self.arre.agregar(objeto)
        archivo.close()

    def mostrar(self):
     for x in range(0,self.arre.actual()):
      print(self.arre.a(x).dni())

    def horas(self):
        print('ingresar dni de la persona y cantidad de horas trabajadas')
        dni = input('dni ')
        for x in range(0,self.arre.actual()):
            if self.arre.a(x).dni() == dni:
                if self.arre.a(x).clase() == empcontratado:
                    horas = input('horas ')
                    self.arre.a(x).gethora(horas)
                    print('horas registradas ' + self.arre.a(x).horas())
                else:
                 print('tipo de empleado no contratado')
        print('tipo de empleado no contratado')
        print('------------------------------------------------')

    def tarea(self):
     print('tareas: carpinteria, electricidad, plomeria')
     ta = input()
     total = 0
     today = datetime.today()
     for x in range(self.arre.actual()):
         if self.arre.a(x).clase() == empexterno:
             if self.arre.a(x).tarea() == ta:
                 if today < self.arre.a(x).fecha():
                  total = total + int(self.arre.a(x).costoobra())
     print('costo total de obra ' + str(total))
     print('---------------------------------------------------')

    def ayuda(self):
      print('----------------ayuda solidaria----------------')
      for x in range(self.arre.actual()):
          if self.arre.a(x).sueldo() < 25000:
            print('-----------------------------------------')
            self.arre.a(x).lista()

    def listar(self):
        for x in range(self.arre.actual()):
            print('--------------------------------------')
            print(self.arre.a(x).nombre())
            print(self.arre.a(x).tele())
            print(self.arre.a(x).sueldo())

    def gastosSueldoPorEmpleado(self,dni):
        empleado = self.buscarpordni(dni)
        if empleado == None:
            print('dni no encontrado')
        else:
         print(empleado.sueldo())

    def modificarBasicoEPlanta(self,dni,nuevoBasico):
        empleado = self.buscarpordni(dni)
        if empleado == None:
            print('dni no encontrado')
        else:
         if empleado.tipo() == 'empleado planta':
            empleado.setsueldo(nuevoBasico)
            print('sueldo basico actualizado')
         else:
             print('no es empleado de planta')
    def modificarViaticoEExterno(self,dni,nuevoViatico):
        empleado = self.buscarpordni(dni)
        if empleado == None:
            print('dni no encontrado')
        else:
            if empleado.tipo() == 'empleado externo':
                empleado.setsueldo(nuevoViatico)
                print('valor viatico actualizado')
            else:
                print('no es empleado externo')
    def modificarValorEPorHora(self,dni,nuevoValorHora):
        empleado = self.buscarpordni(dni)
        if empleado == None:
            print('dni no encontrado')
        else:
            if empleado.tipo() == 'empleado contratado':
                empleado.setsueldo(nuevoValorHora)
                print('valor por hora actualizado')
            else:
                print('no es empleado empleado contratado')

    def contar(self):
     cont = 0
     archivo = open('planta.csv')
     reader = csv.reader(archivo, delimiter=(','))
     for fila in reader:
         cont+= 1
     archivo.close()
     archivo = open('contratados.csv')
     reader = csv.reader(archivo, delimiter=(','))
     for fila in reader:
         cont += 1
     archivo.close()
     archivo = open('externos.csv')
     reader = csv.reader(archivo, delimiter=(','))
     for fila in reader:
         cont += 1
     archivo.close()
     return cont

    def buscarpordni(self, dni):
        empleado = None
        band = False
        i = 0
        while i < self.arre.actual() and not band:
         if self.arre.a(i).dni() == dni:
          band = True
         else:
          i += 1
         if band:
          empleado = self.arre.a(i)
        return empleado