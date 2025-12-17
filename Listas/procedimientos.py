from Listas.lista_enlazada import ListaDobleEnlazada, NodoDoble

class Solicitud:
    def __init__(self, id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo):
        self.id = id
        self.cliente = cliente
        self.tipo = tipo
        self.prioridad = prioridad
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.tiempo = tiempo

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def encolar(self, id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo):

        solicitud = Solicitud(id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo)
        nodo = NodoDoble(solicitud)

        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            nodo.anterior = self.ultimo
            self.ultimo.siguiente = nodo
            self.ultimo = nodo

    def desencolar(self):
        if self.primero is None:
            return None
        temp = self.primero
        self.primero = temp.siguiente
        if self.primero is not None:
            self.primero.anterior = None
        else:
            self.ultimo = None
        return temp

    def desencolarN(self, n):
        solicitudesDesencoladas = ListaDobleEnlazada("Solicitudes Desencoladas")
        i = 0 
        while i < n :
            solicitud = self.desencolar()
            if solicitud is None:
                print("No hay más solicitudes en la cola.")
                print("Se han procesado", i, "solicitudes.")
                break
            solicitudesDesencoladas.insertar(solicitud.contenido)
            i += 1
        return solicitudesDesencoladas
    
    def desencolarPrioridad(self):
        if self.primero is None:
            return None

        actual = self.primero
        nodoConPrioridadAlta = actual.contenido 
        prioridadMaxima = int(actual.contenido.prioridad)

        while actual is not None:
            prioridadActual = int(actual.contenido.prioridad)
            if prioridadActual > prioridadMaxima:
                nodoConPrioridadAlta = actual.contenido
                prioridadMaxima = prioridadActual
            actual = actual.siguiente
        
        self.eliminarSolicitud(nodoConPrioridadAlta.id)
        return nodoConPrioridadAlta
    
    def eliminarSolicitud(self, id):
        actual = self.primero
        while actual is not None:
            solicitud = actual.contenido
            if solicitud.id == id:
                # Caso 1: Es el único nodo
                if self.primero == self.ultimo:
                    self.primero = None
                    self.ultimo = None
                    return solicitud
                # Caso 2: Es el primer nodo (pero hay más)
                elif actual == self.primero:
                    self.primero = actual.siguiente
                    if self.primero is not None:
                        self.primero.anterior = None
                    return solicitud
                # Caso 3: Es el último nodo (pero hay más)
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    if self.ultimo is not None:
                        self.ultimo.siguiente = None
                    return solicitud
                # Caso 4: Es un nodo intermedio
                else:
                    if actual.anterior is not None:
                        actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior
                    return solicitud
            actual = actual.siguiente
        
        print("No se encuentra en la lista.")
        return None

    def verSolicitudes(self):
        actual = self.primero
        while(actual != None):
            solicitud = actual.contenido
            id = solicitud.id
            cliente = solicitud.cliente
            tipo = solicitud.tipo
            prioridad = solicitud.prioridad
            cpu = solicitud.cpu
            ram = solicitud.ram
            print("")
            print(f"Solicitud: {solicitud.id} - {cliente} - ({tipo}) - Prioridad: {prioridad} ")
            print("Estado: Pendiente")
            print(f"Recursos: CPU = {cpu}, Ram = {ram} GB")
            actual = actual.siguiente    
