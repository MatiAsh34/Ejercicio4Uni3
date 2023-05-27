from Empleado import *

class Empleado_Externo(Empleado):
	def __init__(self,dni,nombre,direccion,telefono,tarea,fecha_inicio,fecha_finalizacion,monto_viatico,costo_obra,monto_seguro):
		super().__init__(dni,nombre,direccion,telefono)
		self.__tarea = tarea
		self.__fecha_inicio = fecha_inicio
		self.__fecha_finalizacion = fecha_finalizacion
		self.__monto_viatico = monto_viatico
		self.__costo_obra = costo_obra
		self.__monto_seguro = monto_seguro
		
	def getSueldo(self):
		return self.__costo_obra - self.__monto_viatico - self.__monto_seguro

	def getTarea(self):
		return self.__tarea

	def getCostoObra(self):
		return self.__costo_obra