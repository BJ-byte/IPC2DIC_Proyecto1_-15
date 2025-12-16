from Parser.Parser import Leer_XML

lista_Centros = None

def menu():

    global lista_Centros
    
    while True:
        print("\n----- MENÚ PRINCIPAL -----")
        print("1. Cargar Archivo XML")
        print("2. Gestion de Centros de Datos")
        print("3. Gestion de Máquinas Virtuales")
        print("4. Gestion de Contenedores")
        print("5. Gestion de Solicitudes")
        print("6. Reportes en Graphviz")
        print("7. Generar XML de Salida")
        print("8. Historial de Operaciones")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            
            print("Ingresa la ruta de tu archivo: ")
            ruta = input()
            lista_Centros = Leer_XML(ruta)
            
        elif opcion == "2":
            
            while True:
                print("\n----- Gestion de Centros de Datos -----")
                print("1. Listar Centros de datos")
                print("2. Buscar CEntro por ID")
                print("3. Mostrar Centro con más recursos")
                print("4. Salir")
        
                opcioninterna = input("Selecciona una Opcion")
        
                if opcioninterna == "1":
        
                    imprimirCentros()
        
                elif opcioninterna == "2":
                    print("mas cosas")
        
                elif opcioninterna == "3":
                    print("y mas cosas")
        
                elif opcioninterna == "4":
                    print("Saliendo al Menu Principal")
                    menu()
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
                
            
        elif opcion == "3":
            
            while True:
                print("\n----- Gestion de Máquinas Virtuales -----")
                print("1. Buscar Maquina Virtual por ID")
                print("2. Lista de Maquinas Virtualres de un Centro")
                print("3. Migrar Maquina Virtual")
                print("4. Salir")
        
                opcioninterna = input("Selecciona una Opcion")
        
                if opcioninterna == "1":
        
                    print("cosas xd")
        
                elif opcioninterna == "2":
                    print("mas cosas")
        
                elif opcioninterna == "3":
                    print("y mas cosas")
        
                elif opcioninterna == "4":
                    print("Saliendo al Menu Principal")
                    menu()
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
        
        elif opcion == "4":
            
            while True:
                print("\n----- Gestion de Contenedores -----")
                print("1. Desplegar Contenedor en Maquina Virtual")
                print("2. Lista de Contenedores en una Maquina Virtual")
                print("3. Cambiar el estado de un contenedor")
                print("4. Eliminar contenedor")
                print("5. Salir")
        
                opcioninterna = input("Selecciona una Opcion")
        
                if opcioninterna == "1":
        
                    print("cosas xd")
        
                elif opcioninterna == "2":
                    print("mas cosas")
        
                elif opcioninterna == "3":
                    print("y mas cosas")
        
                elif opcioninterna == "4":
                    print("y mas cosas")
        
                elif opcioninterna == "5":
                    print("Saliendo al Menu Principal")
                    menu()
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
                    
        elif opcion == "5":
            
            while True:
                print("\n----- Gestion de solicitudes -----")
                print("1. Agregar Solicitud")
                print("2. Procesar solicitud de mayor prioridad")
                print("3. Procesar N solicitudes")
                print("4. Ver cola de solicitudes")
                print("5. Salir")
        
                opcioninterna = input("Selecciona una Opcion")
        
                if opcioninterna == "1":
        
                    print("cosas xd")
        
                elif opcioninterna == "2":
                    print("mas cosas")
        
                elif opcioninterna == "3":
                    print("y mas cosas")

                elif opcioninterna == "4":
                    print("y mas cosas")
        
                elif opcioninterna == "5":
                    print("Saliendo al Menu Principal")
                    menu()
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
        
        elif opcion == "6":
            
            print("cosas que no creo que hagamos :v")
        
        elif opcion == "7":

            print("mas cosas que no creo que hagamos, o tal vez si")
        
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def imprimirCentros():
    global lista_Centros
    
    indice = 1
    
    if lista_Centros is None or lista_Centros.primero is None:
        print("No hay centros cargados. Use 'Cargar Archivo XML'.")
        return

    actual = lista_Centros.primero
    
    while actual is not None:
        
        centro = actual.contenido
        print("-----------------------------------------------------------------------------------------------------")
        print(indice,". ID: ", centro.id, "Nombre:", centro.nombre)
        actual = actual.siguiente
        indice = indice + 1
        
def calculoRecursos():
    
    print

menu()