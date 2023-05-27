from ManejadorEmpleado import *

if __name__ == '__main__':
	tamaño = int(input("Ingrese el tamaño del arreglo: "))
	Manejador_Empleado = ManejadorEmpleado(tamaño)
	Manejador_Empleado.Crear_EmpleadoPlanta()
	Manejador_Empleado.Crear_EmpleadoContratado()
	Manejador_Empleado.Crear_EmpleadoExterno()

	opcion = None
	while opcion != '0':
			print("\n1- Ingresar el DNI de un empleado y la cantidad de horas trabajadas en el día")
			print("2- Dada una tarea mostrar el monto a pagar para ella")
			print("3- Listar nombre, dirección y DNI de los empleados cuyo sueldo sea inferior a $15000")
			print("4- Mostrar nombre, teléfono y sueldo a cobrar de todos los empleados.")
			print("0- Salir")
			opcion = input("\nIngrese opcion: ")
   
			if opcion == '1':
				dni = input("Ingrese dni del empleado: ")
				horas = int(input("Ingrese cantidad de horas trabajadas: "))
				Manejador_Empleado.RegistrarHoras(dni,horas) 

			elif opcion == '2':
				tarea = input("\nIngrese nombre de tarea: ")
				Manejador_Empleado.Mostrar_MontoTarea(tarea)
				
			elif opcion == '3':
				Manejador_Empleado.AyudaEconomica()

			elif opcion == '4':
				Manejador_Empleado.MuestraDatos()

			elif opcion == '0':
				print ("Saliendo...")