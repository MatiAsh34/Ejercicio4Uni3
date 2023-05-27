from Empleado import *

class Empleado_Planta(Empleado):
	def __init__(self,dni,nombre,direccion,telefono,sueldo_basico,antiguedad):
		super().__init__(dni,nombre,direccion,telefono)
		self.__sueldo_basico = sueldo_basico
		self.__antiguedad = antiguedad

	def getSueldo(self):
		return self.__sueldo_basico+(self.__sueldo_basico*self.__antiguedad)*0.01