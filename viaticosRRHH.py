import os
import csv



def cargar_datos(archivo,campos):
    lista_rrhh=[]
    cargar = "si"

    if os.path.exists(archivo):
        while (True):
            actualizar = input ("El archivo existe! \n ¿Desea actualizar los datos existentes ? : ")

            if actualizar == "si":
                with open(archivo, 'r') as file:
                    lectura_csv = csv.DictReader(file)
                    
                    for linea in lectura_csv:
                        lista_rrhh.append(linea)
                break
            elif actualizar == "no":
                break
            else:
                print("Vuelva a escribir el nombre del archivo : ")

    while cargar == "si":
        empleado = {}
        for linea in campos:
            while (True):
                dato = input(f"Ingrese {linea} del empleado :  ")

                if (linea == "LEGAJO" ):
                    try:
                        dato = int(dato)
                        empleado[linea] = dato
                        break
                    except:
                        print("El legajo debe ser un numero entero !!!\n Vuelva a intentar : ")
                        
                else:
                    empleado[linea] = dato
                    break

        lista_rrhh.append(empleado)

        cargar = input ("¿Desea seguir añadiendo empleados ? si/no: ")

    try:
        with open(archivo, 'w', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)
            file_guarda.writeheader()
            file_guarda.writerows(lista_rrhh)
            print("Los cambios se guardaron exitosamente !! ")
            return
    except IOError:
        print("ocurrio un error con el archivo! ")
        

def menu():
    while True:
        print("Elija una opcion: \n 1. Cargar datos \n 3.Salir : ")
        opcion = input(" ")
        
        if opcion == "1":
        
            new_archivo = input("Ingese el nombre del archivo que desea guardar : ")
            new_campos = ['LEGAJO','APELLIDO', 'NOMBRE']
            cargar_datos(new_archivo,new_campos)

        if opcion == "3":
            exit()
        else :
            print(" Opción invalida ! repita ")

menu()