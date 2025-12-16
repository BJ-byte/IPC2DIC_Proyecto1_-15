class NodoDoble:
    def __init__(self, contenido):
        self.contenido = contenido
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self, nombreLista):
        self.nombreLista = nombreLista # Debe ser el id del componente que creo esta lista, para implementar buscquda de componentes
        self.primero = None
        self.ultimo = None
    
    def insertar(self, contenido):
        nodo = NodoDoble(contenido)

        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            self.ultimo.siguiente = nodo
            nodo.anterior = self.ultimo
            self.ultimo = nodo

    # Esta funcion considera el primer y ultimo nodo, por ello enlaza su anterior y siguiente solo si existen
    def eliminar(self, contenido):
        actual = self.primero

        while actual is not None:
            if actual.contenido == contenido:
                nodoAnterior = actual.anterior
                nodoSiguiente = actual.siguiente

                if nodoAnterior and (nodoSiguiente is not None):
                    nodoAnterior.siguiente = nodoSiguiente
                    nodoSiguiente.anterior = nodoAnterior

                actual.siguiente = None
                actual.anterior = None
                return actual
            else:
                actual = actual.siguiente
        
        print("No se encuentra en la lista.")

    def buscarXID(self , id):
        actual = self.primero
        
        while actual is not None:
            if actual.contenido.id == id:
                return actual.contenido
            actual = actual.siguiente
        return None

    def nodoConMasRecursos():
        actual = self.primero
        nodoConMasRecursos = actual.contenido

        cpu = int(actual.cpu)
        ram = int(actual.ram)
        almacenamiento = int(actual.almacenamiento)

        cpu2 = int(nodoConMasRecursos.cpu)
        ram2 = int(nodoConMasRecursos.ram)
        almacenamiento2 = int(nodoConMasRecursos.almacenamiento)

        while actual is not None:
            if cpu > cpu2 and ram > ram2 and almacenamiento > almacenamiento2:
                nodoConMasRecursos = actual.contenido
            actual = actual.siguiente