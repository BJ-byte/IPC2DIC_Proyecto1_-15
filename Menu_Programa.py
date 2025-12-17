from Listas.componentes import Centro, MaquinaVirtual, Contenedor, ListaDobleEnlazada
from FuncionesMenu.FuncionesMenu import BuscarMaquinaVirtual, ImprimirMaquinasVirtualesDelCentro, agregarSolicitud, imprimirCentros, buscarcentro, centroConMasRecursos, CargarArchivoXML, migrarMaquinaVirtual, procesarNSolicitudes, procesarSolicitudDeMayorPrioridad, verColaSolicitudes

def menu():
    
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
            
            CargarArchivoXML()
            
        elif opcion == "2":
            
            while True:
                print("\n----- Gestion de Centros de Datos -----")
                print("1. Listar Centros de datos")
                print("2. Buscar CEntro por ID")
                print("3. Mostrar Centro con más recursos")
                print("4. Salir")
        
                opcioninterna = input("Selecciona una Opcion: \n")
        
                if opcioninterna == "1":
        
                    imprimirCentros()
        
                elif opcioninterna == "2":
                    
                    buscarcentro()
        
                elif opcioninterna == "3":
                
                    centroConMasRecursos()
        
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
        
                opcioninterna = input("Selecciona una Opcion: \n")
        
                if opcioninterna == "1":
        
                    print("Ingresa la ID de la Maquina Virtual que deseas buscar: \n")
                    id_vm = input()
                    BuscarMaquinaVirtual(id_vm)
        
                elif opcioninterna == "2":
                    print("Ingresa la ID del Centro del que quieres ver sus Maquinas Virtuales: \n")
                    id = input() 
                    ImprimirMaquinasVirtualesDelCentro(id)
        
                elif opcioninterna == "3":
                    migrarMaquinaVirtual()
        
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
        
                opcioninterna = input("Selecciona una Opcion: \n")
        
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
        
                opcioninterna = input("Selecciona una Opcion: \n")
        
                if opcioninterna == "1":
                    agregarSolicitud()
        
                elif opcioninterna == "2":
                    procesarSolicitudDeMayorPrioridad()
        
                elif opcioninterna == "3":
                    procesarNSolicitudes()

                elif opcioninterna == "4":
                    verColaSolicitudes()
        
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
        
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

menu()
