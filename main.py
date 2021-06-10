from manejadorempleados import  manejador
from login import login
from ingerente import IGerente
from itesorero import ITesorero
def menu():
 print('1 - agregar horas de trabajo de un empleado contratado')
 print('2 - ver costo total de una tarea')
 print('3 - lista de todos empleados que recibiran la ayuda')
 print('4 - listar informacion y sueldo de todos los empleados')
 print('5 - Logearse')
 print('6 - ingresar como tesorero y usar funcion ')
 print('7 - ingresar como gerente y usar funcion')
 print('ingrese cualquier otro numero para terminar.')

def tesorero(usuario):
  dni = input('Ingrese dni de empleado: ')
  usuario.gastosSueldoPorEmpleado(dni)
def menugerente():
 print('elegir opcion')
 print('[1]- Modificar sueldo básico emplado de planta')
 print('[2]- Modificar pago por hora empleado contratado')
 print('[3]- Modificar viatico de empleado externo')
 print('[0]- Volver al menu principal')

def gerente(usuario):
 band = True
 while band == True:
  menugerente()
  op = int(input())
  if op == 1:
   dni = input('Ingrese dni de empleado de planta: ')
   basico = input('Ingrese nuevo sueldo basico: ')
   usuario.modificarBasicoEPlanta(dni, basico)
  elif op == 2:
   dni = input('Ingrese dni de empleado contratado: ')
   valor = input('Ingrese nuevo valor por hora: ')
   usuario.modificarValorEPorHora(dni, valor)
  elif op == 3:
   dni = input('Ingrese dni de empleado externo: ')
   viatico = input('Ingrese nuevo valor de viatico: ')
   usuario.modificarViaticoEExterno(dni, viatico)
  else:
    band = False
print('regreso enu principal')


if __name__ == '__main__':
 maneja = manejador()
 log = login()
 usuario = 'comun'
 band = True
 while band == True:
  menu()
  op = input('ingresar opcion ')
  if op == '1':
   maneja.horas()
  elif op == '2':
   maneja.tarea()
  elif op == '3':
   maneja.ayuda()
  elif op == '4':
   maneja.listar()
  elif op == '6':
   usuario = log.getnivel()
   if usuario == 'tesorero':
    tesorero(ITesorero(maneja))
   else:
    print('acceso denegado')
    print('necesita entrar como tesorero para usar esta funcion')
  elif op == '7':
    usuario = log.getnivel()
    if usuario == 'gerente':
     gerente(IGerente(maneja))
    else:
     print('acceso denegado')
     print('necesita entrar como gerente para usar esta funcion')
  elif op == '5':
   log.login()
  else:
   print('opcion incorrecta')
   band = False
 print('programa terminado')