# Lista madre
# nodo1      ->     nodo2       ->      nodo3  
#  \-centro1          
#         \-nodo1      ->     nodo2       ->      nodo3 
#              \-maquinaVirtual
#                   \-nodo1      ->     nodo2       ->      nodo3 

from Listas.lista_enlazada import ListaDobleEnlazada

class Centro:
    def __init__(self, id, nombre, pais, ciudad, cpu, ram, almacenamiento):
        self.id = id
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad

        self.cpu_original = cpu
        self.ram_original = ram
        self.almacenamiento_original = almacenamiento

        self.cpu_disponible = 0
        self.ram_disponible = 0
        self.almacenamiento_disponible = 0

        self.cpu_usado = 0
        self.ram_usada = 0 
        self.almacenamiento_usado = 0

        self.listaMaquinasVirtuales = ListaDobleEnlazada("VM's de: " + id)

    def CalcularConsumoCentro(self):

        self.cpu_usado = 0
        self.ram_usada = 0
        self.almacenamiento_usado = 0

        actual = self.listaMaquinasVirtuales.primero

        while actual is not None:
            vm = actual.contenido
            self.cpu_usado += int(vm.cpu)
            self.ram_usada += int(vm.ram)
            self.almacenamiento_usado += int(vm.almacenamiento)
            actual = actual.siguiente

    def CalcularRecursosDisponibles(self):

        self.cpu_disponible = 0
        self.ram_disponible = 0
        self.almacenamiento_disponible = 0

        self.cpu_disponible = (int(self.cpu_original) - int(self.cpu_usado))
        self.ram_disponible = (int(self.ram_original) - int(self.ram_usada))
        self.almacenamiento_disponible = (int(self.almacenamiento_original) - int(self.almacenamiento_usado))

class MaquinaVirtual:
    def __init__(self, id, centroAsignado, so, cpu, ram, almacenamiento, ip, estado):
        self.id = id
        self.centroAsignado = centroAsignado
        self.so = so
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.ip = ip
        self.estado = estado
        self.listaContenedores = ListaDobleEnlazada("Contenedores de: " + id)
        

class Contenedor:
    def __init__(self, id, nombre, imagen, cpu, ram, puerto):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen
        self.cpu = cpu
        self.ram = ram
        self.puerto = puerto