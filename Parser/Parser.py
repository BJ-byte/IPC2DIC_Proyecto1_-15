from xml.dom import minidom 

def Leer_XML(ruta_archivo):
    
    try:
        doc = minidom.parse(ruta_archivo)
        
        centrosDatos = doc.getElementsByTagName('centro')
        
        for centro in centrosDatos:
            
            cd_id = centro.getAttribute('id')
            if not cd_id:  
                continue
            cd_nombre = centro.getAttribute('nombre')
            
            cd_ubicacion = centro.getElementsByTagName('ubicacion')[0]
            cd_pais = cd_ubicacion.getElementsByTagName('pais')[0].firstChild.data
            cd_ciudad = cd_ubicacion.getElementsByTagName('ciudad')[0].firstChild.data
            
            cd_capacidad = centro.getElementsByTagName('capacidad')[0]
            cd_cpu = cd_capacidad.getElementsByTagName('cpu')[0].firstChild.data
            cd_ram = cd_capacidad.getElementsByTagName('ram')[0].firstChild.data
            cd_almacenamiento = cd_capacidad.getElementsByTagName('almacenamiento')[0].firstChild.data
            
            print("-----------------------------------------------------------------------------------------------------")
            print("Centro ID: ", cd_id, "Nombre del centro: ", cd_nombre,"\n")
            print("Pais de ubicacion del centro: ", cd_pais, "Ciudad de ubicacion del centro: ", cd_ciudad, "\n")
            print("Recursos del Centro: \n")
            print("CPU: ", cd_cpu, "Ram: ", cd_ram, "Almacenamiento: ", cd_almacenamiento, "\n")
            print("-----------------------------------------------------------------------------------------------------")
            
        maq_virt = doc.getElementsByTagName('vm')
        
        for mv in maq_virt:
            
            mv_id = mv.getAttribute('id')
            mv_centroAsignado = mv.getAttribute('centroAsignado')
            
            mv_SO = mv.getElementsByTagName('sistemaOperativo')[0].firstChild.data
            
            mv_recursos = mv.getElementsByTagName('recursos')[0]
            mv_cpu = mv_recursos.getElementsByTagName('cpu')[0].firstChild.data
            mv_ram = mv_recursos.getElementsByTagName('ram')[0].firstChild.data
            mv_almacenamiento = mv_recursos.getElementsByTagName('almacenamiento')[0].firstChild.data
            
            mv_ip = mv.getElementsByTagName('ip')[0].firstChild.data
            
            print("-----------------------------------------------------------------------------------------------------")
            print("ID de la maquina virtual: ", mv_id, "Centro asignado para la maquina virtual: ", mv_centroAsignado, "\n")
            print("Sistema operativo de la maquina virtual: ", mv_SO, "\n")
            print("Recursos de la maquina virtual: \n" )
            print("CPU: ", mv_cpu, "Ram: ", mv_ram, "Almacenamiento: ", mv_almacenamiento, "\n")
            print("IP de la maquina virtual: ", mv_ip, "\n")
            print("-----------------------------------------------------------------------------------------------------")
            
            contenedores = mv.getElementsByTagName('contenedor')
            
            for mv_contenedor in contenedores:
                
                mv_contenedor_id = mv_contenedor.getAttribute('id')
                mv_contenedor_nombre = mv_contenedor.getElementsByTagName('nombre')[0].firstChild.data
                mv_contenedor_imagen = mv_contenedor.getElementsByTagName('imagen')[0].firstChild.data
            
                mv_contenedor_recursos = mv_contenedor.getElementsByTagName('recursos')[0]
                mv_contenedor_cpu = mv_contenedor_recursos.getElementsByTagName('cpu')[0].firstChild.data
                mv_contenedor_ram = mv_contenedor_recursos.getElementsByTagName('ram')[0].firstChild.data
            
                mv_contenedor_puerto = mv_contenedor.getElementsByTagName('puerto')[0].firstChild.data

                print("-----------------------------------------------------------------------------------------------------")
                print("Contenedores: \n")
                print("ID del contenedor: ", mv_contenedor_id, "Nombre del contenedor: ", mv_contenedor_nombre, "Imagen del contenedor: ", mv_contenedor_imagen, "\n")
                print("Recursos del contenedor: \n")
                print("CPU: ", mv_contenedor_cpu, "Ram: ", mv_contenedor_ram, "\n")
                print("Puerto del contenedor: ", mv_contenedor_puerto, "\n")
                print("-----------------------------------------------------------------------------------------------------")
            
            
            
        solicitudes = doc.getElementsByTagName('solicitud')
            
        for solicitud in solicitudes:
            
            solicitud_id = solicitud.getAttribute('id')
            
            solicitud_cliente = solicitud.getElementsByTagName('cliente')[0].firstChild.data
            solicitud_tipo = solicitud.getElementsByTagName('tipo')[0].firstChild.data
            solicitud_prioridad = solicitud.getElementsByTagName('prioridad')[0].firstChild.data
            
            solicitud_recursos = solicitud.getElementsByTagName('recursos')[0]
            solicitud_recursos_cpu = solicitud_recursos.getElementsByTagName('cpu')[0].firstChild.data
            solicitud_recursos_ram = solicitud_recursos.getElementsByTagName('ram')[0].firstChild.data
            solicitud_recursos_almacenamiento = solicitud_recursos.getElementsByTagName('almacenamiento')[0].firstChild.data
            
            solicitud_tiempoEstimado = solicitud.getElementsByTagName('tiempoEstimado')[0].firstChild.data
            
            print("-----------------------------------------------------------------------------------------------------")
            print("ID de la solicitud: ", solicitud_id, "\n")
            print("Cliente de la solicitud: ", solicitud_cliente, "Tipo de solicitud: ", solicitud_tipo, "Prioridad de la solicitud: ", solicitud_prioridad, "\n")
            print("Recursos solicitados: \n")   
            print("CPU: ", solicitud_recursos_cpu, "Ram: ", solicitud_recursos_ram, "Almacenamiento: ", solicitud_recursos_almacenamiento, "\n")
            print("Tiempo estimado de la solicitud: ", solicitud_tiempoEstimado, "\n")
            print("-----------------------------------------------------------------------------------------------------")
            
        instrucciones = doc.getElementsByTagName('instruccion')
            
        for instruccion in instrucciones:
            instruccion_tipo = instruccion.getAttribute('tipo')
                
            if instruccion_tipo == "crearVM":
                
                instruccion_id = instruccion.getElementsByTagName('id')[0].firstChild.data
                instruccion_centro = instruccion.getElementsByTagName('centro')[0].firstChild.data
                instruccion_so = instruccion.getElementsByTagName('so')[0].firstChild.data
                instrucion_cpu = instruccion.getElementsByTagName('cpu')[0].firstChild.data
                instruccion_ram = instruccion.getElementsByTagName('ram')[0].firstChild.data
                instruccion_almacenamiento = instruccion.getElementsByTagName('almacenamiento')[0].firstChild.data
                
                print("-----------------------------------------------------------------------------------------------------")
                print("Instruccion Crear VM: \n")
                print("ID: ", instruccion_id, "Centro: ", instruccion_centro, "SO: ", instruccion_so, "\n")
                print("CPU: ", instrucion_cpu, "Ram: ", instruccion_ram, "Almacenamiento: ", instruccion_almacenamiento, "\n")
                print("-----------------------------------------------------------------------------------------------------")
                
            elif instruccion_tipo == "migrarVM":
                instruccion_mv_id = instruccion.getElementsByTagName('vmId')[0].firstChild.data
                instruccion_centro_origen = instruccion.getElementsByTagName('centroOrigen')[0].firstChild.data
                instruccion_centro_destino = instruccion.getElementsByTagName('centroDestino')[0].firstChild.data
                
                print("-----------------------------------------------------------------------------------------------------")
                print("Instruccion Migrar VM: \n")
                print("ID de la VM: ", instruccion_mv_id, "\nCentro de origen: ", instruccion_centro_origen, "\nCentro de destino: ", instruccion_centro_destino, "\n")
                print("-----------------------------------------------------------------------------------------------------")
                
            elif instruccion_tipo == "procesarSolicitudes":
                instruccion_cantidad_procesar = instruccion.getElementsByTagName('cantidad')[0].firstChild.data
                
                print("-----------------------------------------------------------------------------------------------------")
                print("Instruccion Procesar Solicitudes: \n")
                print("Cantidad a procesar: ", instruccion_cantidad_procesar, "\n")
                print("-----------------------------------------------------------------------------------------------------")
                
            else:
                print("Tipo no reconocido")
                print("-----------------------------------------------------------------------------------------------------")
                return
        
    except Exception as e:
        print(f"A ocurrido un error al tratar de cargar el archivo: {e} ")

__all__ = ['Leer_XML']

