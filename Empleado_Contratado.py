from Empleado import *

class Empleado_Contratado(Empleado):
	__valor_hora = 0
	def __init__(self,dni,nombre,direccion,telefono,fecha_inicio,fecha_finalizacion,cantidad_horas):
		super().__init__(dni,nombre,direccion,telefono)
		self.__fecha_inicio = fecha_inicio
		self.__fecha_finalizacion = fecha_finalizacion
		self.__cantidad_horas = cantidad_horas

	@classmethod
	def setValor_Hora(cls,valor):
		cls.__valor_hora = valor

	def getSueldo(self):
		return self.__cantidad_horas*self.__valor_hora

	def getCantidadHoras(self):
		return self.__cantidad_horas

	def Registrar_CantidadHoras(self,horas):
		self.__cantidad_horas += horas