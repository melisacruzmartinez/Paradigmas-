import os
import csv


# Cargar datos, crear archivos o editarlos.
def cargar_datos(archivo,campos):
    lista_rrhh=[]
    cargar = "si"

    if os.path.exists(archivo):
            actualizar = input ("El archivo existe! \n ¿Desea actualizar los datos existentes ? : ")

            while (True):
                if actualizar == "si":
                    with open(archivo, 'r') as file:
                        lectura_csv = csv.DictReader(file)
                        
                        for linea in lectura_csv:
                            lista_rrhh.append(linea)
                    break
                elif actualizar == "no":
                    return
    else:
        seguir = input("Desea crear el archivo? si/no: ")
            
        if seguir == "no":
            return

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

#B_control de gastos
def gastos(archivo1,archivo2):

    num_legajo = input ("Ingresa el legajo que deseas averiguar: ")

    with open (archivo1, 'r')  as file:
        datos_csv = csv.DictReader(file)

        nombre = "null"

        for fila in datos_csv:
            if (fila["LEGAJO"] == num_legajo):
                nombre = fila["NOMBRE"]

        if (nombre == "null"):
            print("Legajo no encontrado")
            return

        with open (archivo2, 'r')  as f:
            gastos_csv = csv.DictReader(f)

            gasto_total = 0

            for fila in gastos_csv:
                if (fila["Legajo"] == num_legajo):
                    gasto_total += int(fila["Gastos"])

            if (gasto_total > 5000):
                diferencia = gasto_total - 5000
                print(f"Se paso del presupuesto de viaticos con {diferencia} pesos")

            else:
                print("Legajo {} : {}, gasto $ {} en viaticos ".format(num_legajo, nombre, gasto_total))

# A_ menu de acciones 

def menu():
    while True:
        print("Elija una opcion: \n 1. Cargar datos \n 2. Controlar viaticos \n 3.Salir : ")
        opcion = input(" ")
        
        if opcion == "1":
        
            new_archivo = input("Ingese el nombre del archivo que desea guardar : ")
            new_campos = ['LEGAJO','APELLIDO', 'NOMBRE']
            cargar_datos(new_archivo,new_campos)

        elif opcion == "2":
            new_archivo1 = input("Ingese el nombre del archivo1 que guarda los datos de los empleados : ")
            new_archivo2 = input("Ingese el nombre del archivo2 que guarda los gastos de los empleados : ")
            #añadi esta condicional para que no tire error cuando no existe el archivo
            if os.path.exists(new_archivo1) and os.path.exists(new_archivo2):
                gastos(new_archivo1, new_archivo2)
            else:
                print ("Uno o ambos archivos no se encontraron")

        elif opcion == "3":
            print ("Hasta pronto !")
            exit()
        else :
            print(" Opción invalida ! repita ")

menu()