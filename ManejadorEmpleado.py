from Empleado import *
from Empleado_Planta import *
from Empleado_Contratado import *
from Empleado_Externo import *

import numpy as np
import csv

class ManejadorEmpleado(object):
	__cantidad = 0 #elementos cargados en el arreglo
	__dimension = 0 #cuantas componentes tiene el arreglo
	__incremento = 8 #en cuentas unidades se va incrementar el arreglo

	def __init__(self,tamaño):
		self.__dimension = tamaño
		self.__arreglo = np.empty(tamaño,dtype=Empleado)


	def Cargar(self,empleado):
		if self.__cantidad == self.__dimension:
			self.__dimension += self.__incremento
			self.__arreglo.resize(self.__dimension)

		self.__arreglo[self.__cantidad] = empleado
		self.__cantidad += 1


	def Crear_EmpleadoPlanta(self):
		archivo = open('planta.csv',encoding='utf8')
		reader = csv.reader(archivo,delimiter=',')
		
		for fila in reader:
			empleado_planta = Empleado_Planta(fila[0],fila[1],fila[2],fila[3],float(fila[4]),int(fila[5]))
			ManejadorEmpleado.Cargar(self,empleado_planta)


	def Crear_EmpleadoContratado(self):
		archivo = open('contratados.csv',encoding='utf8')
		reader = csv.reader(archivo,delimiter=',')
		i = 0
	
		for fila in reader:
			empleado_contratado = Empleado_Contratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],int(fila[6]))
			ManejadorEmpleado.Cargar(self,empleado_contratado)

			if i == 0:
				empleado_contratado.setValor_Hora(float(fila[7]))
				i += 1
			

	def Crear_EmpleadoExterno(self):
		archivo = open('externos.csv',encoding='utf8')
		reader = csv.reader(archivo,delimiter=',')
		
		for fila in reader:
			empleado_externo = Empleado_Externo(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],float(fila[7]),float(fila[8]),float(fila[9]))
			ManejadorEmpleado.Cargar(self,empleado_externo)


	def RegistrarHoras(self,dni,horas):
		i = 0
		c = 0
		band = False
		while i < len(self.__arreglo) and band == False:
			if self.__arreglo[i] != None:
				if dni == self.__arreglo[i].getDNI():
					self.__arreglo[i].Registrar_CantidadHoras(horas)
					print("\nHoras registradas!")
					print("Horas antiguas: {}, horas actualizadas: {}".format(self.__arreglo[i].getCantidadHoras()-horas,self.__arreglo[i].getCantidadHoras()))
					c = 1
					band = True
				else:
					i += 1
			else:
				band = True
			
		if c != 1:
			print("DNI no encontrada!")		


	def Mostrar_MontoTarea(self,tarea):
		i = 0
		band = False
		monto = 0
		while i < len(self.__arreglo) and band == False:
			if self.__arreglo[i] != None:
				try:
					if tarea == self.__arreglo[i].getTarea():
						monto += self.__arreglo[i].getCostoObra()
				except AttributeError:
					pass
				i += 1
			else:
				band = True
    
		if monto != 0:
			print("El monto a pagar por la tarea es: ",monto)
		else:
			print("Tarea no encontrada!")


	def AyudaEconomica(self):
		i = 0
		band = False
		while i < len(self.__arreglo) and band == False:
			if self.__arreglo[i] != None:
				if self.__arreglo[i].getSueldo() < 15000:
					print("Nombre: {}, Direccion: {}, DNI: {}, Sueldo: {}".format(self.__arreglo[i].getNombre(),self.__arreglo[i].getDireccion(),self.__arreglo[i].getDNI(),self.__arreglo[i].getSueldo()))
				i += 1
			else:
				band = True


	def MuestraDatos(self):
		i = 0
		band = False
		while i < len(self.__arreglo) and band == False:
			if self.__arreglo[i] != None:
				print("Nombre: {}  Telefono: {}  Sueldo: {}".format(self.__arreglo[i].getNombre(),self.__arreglo[i].getTelefono(),self.__arreglo[i].getSueldo()))
				i += 1
			else:
				band = True