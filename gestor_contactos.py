import time  
import os
def agenda():      #Este programa sirve para agregar,modificar,eliminar y consultar contactos de una agenda
	contactos = {}
	salir=True
	while(salir):

		print('Bienvenido A Mi Agenda\n')
		print(' 1.) Ver Contactos\n 2.) Agregar Contacto\n 3.) Buscar Contacto\n 4.) Modificar Contacto\n 5.) Eliminar Contacto\n 6.) Salir\n')
		
		opcion=input('Ingrese opcion: ')
		os.system("cls")
		if opcion == '1': # <----Muestra los contactos
			for contacto in contactos:
				for numero in contactos:
					print('Contacto / Numero')
					print( numero,contactos[contacto])
				
			os.system("cls")

		elif opcion == '2': # <----Registra los contactos
			nombre=input('Nombre: ')
			if nombre in contactos:
				print('Error el contacto ya existe')
				time.sleep(3) # <---- tiempo que muestra en la pantalla el msj, antes de volver a mostrar el menú
				os.system("cls")
				continue      # <----omitimos el codigo restante dentro del ciclo solo para la iteracion actual
			try:
				numero=int(input('Numero: '))
				if numero>9999999999:  # <---- validamos numeros ingresados 
					print('El numero es demaciado largo')
					time.sleep(3)
					os.system("cls")   # <---- limpia pantalla
					continue
				elif numero<1000000000:
					print('El numero es demaciado corto\nDeben de ser 10 digitos')
					time.sleep(2)
					os.system("cls")
					continue
				
			except:
				print('Valor no valido')
				time.sleep(3)
				os.system("cls")
			contactos[(nombre)] = numero
			print('Contacto agregado')
			print(contactos)
			time.sleep(3)
			os.system("cls")

		elif opcion == '3': # <----- Buscar Contacto
			buscar=input('Contacto a Buscar: ')
			print (contactos[buscar])
			time.sleep(3)
			os.system("cls")
			if buscar not in contactos:
				print('El contacto no existe., agreguelo desde el menu')
				continue

		elif opcion == '4': # <------- Modificar contacto
			contacto = input('Contacto a modificar: ')
			if contacto not in contactos:
				print ('El contacto no existe, agreguelo desde el menu')
				continue
			try:                        # <---- probamos el bloque con un try en busca de errores
				nuevo=int(input('Nuevo Numero: '))
				contactos[contacto]=nuevo
				if nuevo>9999999999:
					print('El numero es demaciado largo')
					time.sleep(3)
					os.system("cls")
					continue
				elif nuevo<1000000000:
					print('El numero es muy corto\nDeben de ser 10 digitos')
				print('Contacto modificado con exito')
				time.sleep(3)
				os.system("cls")
				continue
			except:                    # <---- manejamos el error con un except 
				print('¡Dato no valido!')
				time.sleep(3)
				os.system("cls")
				continue

		elif opcion == '5':
			eliminar=input('Contacto a eliminar: ')
			if eliminar not in contactos:
				print ("El contacto no existe")
				continue
			del(contactos[eliminar])         # <---- eliminamos el contacto del diccionario con el bloque del
			print('Contacto',eliminar,'eliminado con exito')
			time.sleep(4)
			os.system("cls")
			continue
		elif opcion == '6': # <---- regresar al menu principal
			print ("programa terminado...")
			break
		else:
			print('Opcion no valida,\nElija una opcion del 1 al 6')
			time.sleep(3)
			os.system("cls")
agenda()


#SUGERENCIA Y CORRECCIONES: 


import time  
import os

def agenda():
    # Este programa sirve para agregar, modificar, eliminar y consultar contactos de una agenda
    contactos = {}
    salir = True

    while salir:
        print('Bienvenido a Mi Agenda\n')
        print(' 1.) Ver Contactos\n 2.) Agregar Contacto\n 3.) Buscar Contacto\n 4.) Modificar Contacto\n 5.) Eliminar Contacto\n 6.) Salir\n')
        opcion = input('Ingrese opción: ')
        os.system("cls")

        if opcion == '1': # Muestra los contactos
            if contactos.__len__ <0:
                 print('No existen contactos aún')
                 time.sleep(2)
                 
            else:
                print('Contacto / Numero')
                for contacto, numero in contactos.items():
                    print(contacto, numero)
                    time.sleep(3)
                
            os.system("cls")

        elif opcion == '2': # Registra los contactos
            nombre = input('Nombre: ')
            if nombre.lower() in contactos:
                print('Error: el contacto ya existe')
                time.sleep(3)
                os.system("cls")
                continue

            try:
                numero = int(input('Número: '))
                if numero > 9999999999:
                    print('El número es demasiado largo')
                    time.sleep(3)
                    os.system("cls")
                    continue
                elif numero < 1000000000:
                    print('El número es demasiado corto. Deben ser 10 dígitos')
                    time.sleep(2)
                    os.system("cls")
                    continue
            except:
                print('Valor no válido')
                time.sleep(3)
                os.system("cls")

            contactos[nombre.lower()] = numero
            print('Contacto agregado')
            print(contactos)
            time.sleep(3)
            os.system("cls")

        elif opcion == '3': # Buscar Contacto
            buscar = input('Contacto a buscar: ')
            buscar = buscar.lower()
            if buscar not in contactos:
                print('El contacto no existe. Agréguelo desde el menú')
                continue

            print('Contacto:', buscar, 'Número:', contactos[buscar])
            time.sleep(3)
            os.system("cls")

        elif opcion == '4': # Modificar contacto
            contacto = input('Contacto a modificar: ')
            contacto = contacto.lower()
            if contacto not in contactos:
                print('El contacto no existe. Agréguelo desde el menú')
                continue

            try:
                nuevo = int(input('Nuevo Número: '))
                contactos[contacto] = nuevo
                if nuevo > 9999999999:
                    print('El número es demasiado largo')
                    time.sleep(3)
                    os.system("cls")
                    continue
                elif nuevo < 1000000000:
                    print('El número es demasiado corto. Deben ser 10 dígitos')
                    time.sleep(3)
                    os.system("cls")
                    continue

                print('Contacto modificado con éxito')
                time.sleep(3)
                os.system("cls")

            except:
                print('Dato no válido')
                time.sleep(3)
                os.system("cls")
                continue

        elif opcion == '5':
            eliminar = input('Contacto a eliminar: ')
            eliminar = eliminar.lower()
            if eliminar not in contactos:
                print("El contacto no existe")
                continue

            del contactos[eliminar]
            print('Contacto', eliminar, 'eliminado con éxito')
            time.sleep(4)
            os.system("cls")
            continue

        elif opcion == '6': # Regresar al menú principal
            print("Programa terminado...")
            break

        else:
            print('Opción no válida. Elija una opción del 1 al 6')
            time.sleep(3)
            os.system("cls")

agenda()
