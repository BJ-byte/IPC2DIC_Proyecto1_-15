from lista_enlazada import NodoDoble

class Solicitud:
    def __init__(self, id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo):
        id = id
        cliente = cliente
        tipo = tipo
        prioridad = prioridad
        cpu = cpu
        ram = ram
        almacenamiento = almacenamiento
        tiempo = tiempo

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def encolar(self, id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo):

        solicitud = Solicitud(ide, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo)
        nodo = NodoDoble(solicitud)

        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            self.ultimo.siguiente = nodo
            self.ultimo = nodo

    def desencolar(self):
        temp = self.inicio
        self.inicio = inicio.siguiente
        return temp

    def desencolarN(self, n):
        i = 0 
        while i < n :
            desencolar()
            i++
    
    def desencolarPrioridad(self):

        nodoMayorPrioridad = sel.siguiente
        nodoActual = self.primero.siguiente

        while nodoActual is not None:
            if nodoActual.prioridad > nodoMayorPrioridad.prioridad:
                nodoMayorPrioridad = nodoActual
                nodoActual = nodoActual.siguiente

        if nodoMayorPrioridad is not None:
            if nodoMayorPrioridad is self.primero:
                desencolar()

            elif nodoMayorPrioridad is self.ultimo:
                self.ultimo = self.ultimo.anterior
                self.ultimo.siguiente = None
                return nodoMayorPrioridad

            else:
                nodoAnterior = nodoMayorPrioridad.anterior
                nodoSiguiente = nodoMayorPrioridad.siguiente
                nodoAnterior.siguiente = nodoSiguiente
                nodoSiguiente.anterior = nodoAnterior
                return nodoMayorPrioridad

    def verSolicitudes(self):
        