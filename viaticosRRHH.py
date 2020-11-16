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