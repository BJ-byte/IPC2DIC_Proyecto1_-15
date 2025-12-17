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
            if actual.contenido == contenido or actual.contenido.id == contenido.id:
                # Caso 1: Es el único nodo
                if self.primero == self.ultimo:
                    self.primero = None
                    self.ultimo = None
                    return actual.contenido
                # Caso 2: Es el primer nodo (pero hay más)
                elif actual == self.primero:
                    self.primero = actual.siguiente
                    if self.primero is not None:
                        self.primero.anterior = None
                    return actual.contenido
                # Caso 3: Es el último nodo (pero hay más)
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    if self.ultimo is not None:
                        self.ultimo.siguiente = None
                    return actual.contenido
                # Caso 4: Es un nodo intermedio
                else:
                    if actual.anterior is not None:
                        actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior
                    return actual.contenido
            actual = actual.siguiente
        
        print("No se encuentra en la lista.")
        return None

    def buscarXID(self , id):
        actual = self.primero
        
        while actual is not None:
            if actual.contenido.id == id:
                return actual.contenido
            actual = actual.siguiente
        return None

    def nodoConMasRecursos(self):
        actual = self.primero
        nodoConMasRecursos = actual.contenido

        cpu = int(actual.contenido.cpu_original)
        ram = int(actual.contenido.ram_original)
        almacenamiento = int(actual.contenido.almacenamiento_original)

        cpu2 = int(nodoConMasRecursos.cpu_original)
        ram2 = int(nodoConMasRecursos.ram_original)
        almacenamiento2 = int(nodoConMasRecursos.almacenamiento_original)

        while actual is not None:
            if cpu > cpu2 and ram > ram2 and almacenamiento > almacenamiento2:
                nodoConMasRecursos = actual.contenido
            actual = actual.siguiente

        return nodoConMasRecursos
    