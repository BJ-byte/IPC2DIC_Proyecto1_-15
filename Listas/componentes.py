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
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.listaMaquinasVirtuales = ListaDobleEnlazada("VM's de: " + id)
        
    def CalcularConsumoCentro(self):
        cpu_usado = 0
        ram_usada = 0
        almacenamiento_usado = 0
    
        actual = self.listaMaquinasVirtuales.primero
        
        while actual is not None:
            vm = actual.contenido
            cpu_usado += int(vm.cpu)
            ram_usada += int(vm.ram)
            almacenamiento_usado += int(vm.almacenamiento)
            actual = actual.siguiente
        return cpu_usado, ram_usada, almacenamiento_usado

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