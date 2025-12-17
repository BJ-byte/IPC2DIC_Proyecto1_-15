from Listas.componentes import MaquinaVirtual
from Listas.procedimientos import Cola
from Parser.Parser import Leer_XML

lista_Centros = None
cola_Solicitudes = None

def CargarArchivoXML():
    global lista_Centros
    global cola_Solicitudes
    print("Ingresa la ruta de tu archivo: ")
    ruta = input()
    lista = Leer_XML(ruta)
    lista_Centros = lista.primero.contenido
    cola_Solicitudes = lista.primero.siguiente.contenido
    print("Archivo cargado exitosamente.")

def centroConMasRecursos():
    
    global lista_Centros
    centro = lista_Centros.nodoConMasRecursos()

    centro.CalcularConsumoCentro()
    centro.CalcularRecursosDisponibles()
        
    porcentaje_cpu = (int(centro.cpu_usado) / int(centro.cpu_original)) * 100
    porcentaje_ram = (int(centro.ram_usada) / int(centro.ram_original)) * 100
    porcentaje_almacenamiento = (int(centro.almacenamiento_usado) / int(centro.almacenamiento_original)) * 100

    print("ID: ", centro.id, " Nombre del centro: ", centro.nombre)
    print("CPU: ", centro.cpu_disponible, " de ", centro.cpu_original, "/    Aproximádamente: ", porcentaje_cpu,"%")
    print("Ram: ", centro.ram_disponible, " de ", centro.ram_original, "/    Aproximádamente: ", porcentaje_ram,"%")
    print("Almacenamiento: ", centro.almacenamiento_disponible, " de ", centro.almacenamiento_original, "/   Aproximádamente: ", porcentaje_almacenamiento,"%")

def buscarcentro():

    global lista_Centros
    
    print("Ingresa la ID del centro que deseas buscar: \n")
    id = input()
    
    centro = lista_Centros.buscarXID(id)
    
    if centro is not None:
        
        centro.CalcularConsumoCentro()
        centro.CalcularRecursosDisponibles()
        
        porcentaje_cpu = (int(centro.cpu_usado) / int(centro.cpu_original)) * 100
        porcentaje_ram = (int(centro.ram_usada) / int(centro.ram_original)) * 100
        porcentaje_almacenamiento = (int(centro.almacenamiento_usado) / int(centro.almacenamiento_original)) * 100
        
        print("ID: ", centro.id, " Nombre del centro: ", centro.nombre)
        print("CPU: ", centro.cpu_disponible, " de ", centro.cpu_original, "/    Aproximádamente: ", porcentaje_cpu,"%")
        print("Ram: ", centro.ram_disponible, " de ", centro.ram_original, "/    Aproximádamente: ", porcentaje_ram,"%")
        print("Almacenamiento: ", centro.almacenamiento_disponible, " de ", centro.almacenamiento_original, "/   Aproximádamente: ", porcentaje_almacenamiento,"%")
    else:
        print("El centro que buscas no existe.\n")
        

def imprimirCentros():
    global lista_Centros
    
    indice = 1
    
    if lista_Centros is None or lista_Centros.primero is None:
        print("No hay centros cargados. Use 'Cargar Archivo XML'.")
        return

    actual = lista_Centros.primero
    
    while actual is not None:
        
        centro = actual.contenido
        centro.CalcularConsumoCentro()
        centro.CalcularRecursosDisponibles()
        
        porcentaje_cpu = (int(centro.cpu_usado) / int(centro.cpu_original)) * 100
        porcentaje_ram = (int(centro.ram_usada) / int(centro.ram_original)) * 100
        porcentaje_almacenamiento = (int(centro.almacenamiento_usado) / int(centro.almacenamiento_original)) * 100
        
        print("-----------------------------------------------------------------------------------------------------")
        print(indice,". ID: ", centro.id, ". Nombre:", centro.nombre)
        print("CPU: ", centro.cpu_disponible, " de ", centro.cpu_original, "/    Aproximádamente: ", porcentaje_cpu,"%")
        print("Ram: ", centro.ram_disponible, " de ", centro.ram_original, "/    Aproximádamente: ", porcentaje_ram,"%")
        print("Almacenamiento: ", centro.almacenamiento_disponible, " de ", centro.almacenamiento_original, "/   Aproximádamente: ", porcentaje_almacenamiento,"%")
        actual = actual.siguiente
        indice = indice + 1

def BuscarMaquinaVirtual(id):
    global lista_Centros
    
    if lista_Centros is None or lista_Centros.primero is None:
        print("No hay centros cargados.")
        return
    
    centro_actual = lista_Centros.primero
    
    while centro_actual is not None:
        
        centro = centro_actual.contenido
        vm_actual = centro.listaMaquinasVirtuales.primero
        
        while vm_actual is not None:
            
            vm = vm_actual.contenido
            
            contador_contenedores = 0
            contenedor_actual = vm.listaContenedores.primero
            
            while contenedor_actual is not None:
                contador_contenedores += 1
                contenedor_actual = contenedor_actual.siguiente
            
            if vm.id == id:
                print("ID:", vm.id)
                print("SO:", vm.so)
                print("Recursos asignados: (CPU: ", vm.cpu, ", RAM: ", vm.ram, ")")
                print("Estado:", vm.estado)
                print("IP:", vm.ip)
                print("Centro:", centro.nombre)
                print("Número de contenedores desplegados:", contador_contenedores)
            
            vm_actual = vm_actual.siguiente
        
        centro_actual = centro_actual.siguiente
    print("No se encontró la máquina virtual con ID:", id)

def ImprimirMaquinasVirtualesDelCentro(id):
    
    global lista_Centros
    
    if lista_Centros is None or lista_Centros.primero is None:
        print("No hay centros cargados.")
        return
    
    centro_buscado = lista_Centros.buscarXID(id)
    
    if centro_buscado is None:
        print("No se encontró el centro con ID:", id)
        return
    
    if centro_buscado.listaMaquinasVirtuales.primero is None:
        print("No hay máquinas virtuales en este centro.")
        return
    
    print("\nMáquinas virtuales del centro:", centro_buscado.nombre, "\n")
    print("-----------------------------------------------------")
    
    vm_actual = centro_buscado.listaMaquinasVirtuales.primero
    contador_contenedores = 1
            
    while vm_actual is not None:

        vm = vm_actual.contenido
        contador_contenedores = 0
        contenedor_actual = vm.listaContenedores.primero
            
        while contenedor_actual is not None:
            contador_contenedores += 1
            contenedor_actual = contenedor_actual.siguiente
        
        print("ID:", vm.id)
        print("SO:", vm.so)
        print("Recursos asignados: (CPU: ", vm.cpu, ", RAM: ", vm.ram, ")")
        print("Estado:", vm.estado)
        print("IP:", vm.ip)
        print("Número de contenedores desplegados:", contador_contenedores)
        print("-----------------------------------------------------")
                
        vm_actual = vm_actual.siguiente

def agregarSolicitud():
    global cola_Solicitudes

    if cola_Solicitudes is None:
        cola_Solicitudes = Cola()
    print("")
    id = input("Ingrese ID de la solicitud: ")
    cliente = input("Ingrese el nombre del cliente: ")
    tipo = input("Ingrese el tipo de solicitud (Deploy o Backup): ")
    prioridad = input("Ingrese la prioridad de la solicitud (1-10): ")
    cpu = input("Ingrese la cantidad de CPU requerida: ")
    ram = input("Ingrese la cantidad de RAM requerida: ")
    almacenamiento = input("Ingrese la cantidad de Almacenamiento requerida: ")
    tiempo = input("Ingrese el tiempo estimado de la solicitud: ")

    cola_Solicitudes.encolar(id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo)
    print("Solicitud agregada exitosamente.")

def procesarSolicitudDeMayorPrioridad():
    if cola_Solicitudes is None or cola_Solicitudes.primero is None:
        print("No hay solicitudes en la cola.")
    else:
        solicitudProcesada = cola_Solicitudes.desencolarPrioridad()
        if solicitudProcesada is not None:
            print("Procesando solicitud de ID:", solicitudProcesada.id)
            procesarSolicitud(solicitudProcesada)
            print("Solicitud procesada:", solicitudProcesada.id, "Cliente:", solicitudProcesada.cliente)

        else:
            print("No hay solicitudes en la cola.")

def procesarNSolicitudes():
    if cola_Solicitudes is None:
        print("No hay solicitudes en la cola.")
    else:
        n = int(input("Ingrese el número de solicitudes a procesar: "))
        solicitudProcesadas = cola_Solicitudes.desencolarN(n)
        solicitudActual = solicitudProcesadas.primero
        while solicitudActual is not None:
            solicitudProcesada = solicitudActual.contenido
            print("Procesando solicitud de ID:", solicitudProcesada.id)
            procesarSolicitud(solicitudProcesada)
            print("Solicitud procesada:", solicitudProcesada.id, "Cliente:", solicitudProcesada.cliente)
            solicitudActual = solicitudActual.siguiente

def verColaSolicitudes():
    if cola_Solicitudes is None:
        print("No hay solicitudes en la cola.")
    else:
        print("Cola de Solicitudes:")
        cola_Solicitudes.verSolicitudes()

def crearMV(id, centroAsignado, so, cpu, ram, almacenamiento, ip, estado):
    mv = MaquinaVirtual(id, centroAsignado, so, cpu, ram, almacenamiento, ip, estado)
    confirmarCentro = lista_Centros.buscarXID(centroAsignado)
    if confirmarCentro is None:
        print("El centro asignado a la maquina virtual no existe")
        return None

    actual = lista_Centros.primero
    while actual is not None:
        centro = actual.contenido
        if centro.id == centroAsignado:
            if validarRecursosDisponibles(centro, cpu, ram, almacenamiento):
                centro.listaMaquinasVirtuales.insertar(mv)
                print("Maquina Virtual creada exitosamente en el centro:", centroAsignado)
                return mv
            else:
                print("No hay recursos disponibles en el centro asignado.")
                return None
        actual = actual.siguiente

def validarRecursosDisponibles(contenidoNodo, cpu, ram, almacenamiento):

    contenidoNodo.CalcularRecursosDisponibles()
    contenidoNodo.CalcularConsumoCentro()

    cpuFinal = int(contenidoNodo.cpu_disponible) - int(cpu)
    ramFinal = int(contenidoNodo.ram_disponible) - int(ram)
    almacenamientoFinal = int(contenidoNodo.almacenamiento_disponible) - int(almacenamiento)

    if cpuFinal < 0 or ramFinal < 0 or almacenamientoFinal < 0:
        return False    
    return True

def eliminarMV(centroOrigen, idMV, centroDestino):
    
    if lista_Centros.buscarXID(centroOrigen) is None:
        print("El centro origen asignado a la maquina virtual no existe")
        return None
    if lista_Centros.buscarXID(centroDestino) is None:
        print("El centro destino asignado a la maquina virtual no existe")
        return None

    mvMigrar = None

    actual = lista_Centros.primero
    while actual is not None:
        centro = actual.contenido
        if centro.id == centroOrigen:
            lista_mvs = centro.listaMaquinasVirtuales
            if lista_mvs.buscarXID(idMV) is None:
                print("La Maquina Virtual no existe en el centro especificado.")
                return None
            
            nodoActualMv = lista_mvs.primero
            while nodoActualMv is not None:
                if nodoActualMv.contenido.id == idMV:
                    cpu_mv = int(nodoActualMv.contenido.cpu)
                    ram_mv = int(nodoActualMv.contenido.ram)
                    almacenamiento_mv = int(nodoActualMv.contenido.almacenamiento)

                    mvMigrar = nodoActualMv.contenido

                    lista_mvs.eliminar(nodoActualMv.contenido)

                    print("Maquina Virtual eliminada exitosamente del centro:", centroOrigen)
                    print("Recursos liberados: CPU:", cpu_mv, " RAM:", ram_mv, " Almacenamiento:", almacenamiento_mv)
                    print("Migrando maquina virtual...")
                nodoActualMv = nodoActualMv.siguiente
        actual = actual.siguiente
         
    actual = lista_Centros.primero
    while actual is not None:
        centro = actual.contenido
        if centro.id == centroDestino:
            if validarRecursosDisponibles(centro, mvMigrar.cpu, mvMigrar.ram, mvMigrar.almacenamiento):
                centro.listaMaquinasVirtuales.insertar(mvMigrar)
                print("Maquina Virtual migrada exitosamente al centro:", centroDestino)
                return mvMigrar
            else:
                print("No hay recursos disponibles en el centro destino.")
                actual = actual.siguiente
                while actual is not None:
                    centro = actual.contenido
                    if centro.id == centroOrigen:
                        centro.listaMaquinasVirtuales.insertar(mvMigrar)
                        print("La Maquina Virtual ha sido regresada al centro de origen debido a falta de recursos en el centro destino.")
                    actual = actual.siguiente
                return None
        actual = actual.siguiente

def procesarSolicitud(solicitud):
    tipo = solicitud.tipo
    centro = lista_Centros.nodoConMasRecursos()
    if tipo == "Deploy":
        print("Procesando solicitud de Deploy...")
        ip = f"192.168.1.{solicitud.id}"
        crearMV(solicitud.id, centro.id, "Windows Server 2022", solicitud.cpu, solicitud.ram, solicitud.almacenamiento, ip, "Activa")

    elif tipo == "Backup":
        print("Procesando solicitud de Backup...")
        ip = f"192.168.1.{solicitud.id}"
        crearMV(solicitud.id, centro.id, "Windows Server 2022", solicitud.cpu, solicitud.ram, solicitud.almacenamiento, ip, "Suspendida")
    else:
        print("Tipo de solicitud desconocido.")
        print("No se realizo nigun proceso.")

def migrarMaquinaVirtual():
    print("")
    idMV = input("Ingrese id de Maquina Virtual a migrar: ")
    centroOrigen = input("Ingrese centro de origen: ")
    centroDestino = input("Ingrese centro de destino: ")
    eliminarMV(centroOrigen, idMV, centroDestino)