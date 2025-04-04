import logging
from publicacion import Publicacion




def mostrar_menu():
    while True:
        print("\n Gestion de Publicaciones")
        print("1. Crear nueva publicacion")
        print("2. Listar todas las publicaciones")
        print("3. Listar las publicaciones de un usuario especifico")
        print("4. Editar el contenido de una publicacion")
        print("5. Eliminar una publicacion")
        print("6. Volver al menu principal")

        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            crear_publicacion()

        elif opcion == "2":
            listar_publicaciones()





def crear_publicacion():
    print("\n CREACION DE UNA PUBLICACION")
    id_usuario = input("Introduce el ID de usuario: ")
    contenido = input("Contenido: ")

    if not id_usuario or not contenido:
        print("Todos los campos son obligatorios.")
        return
    
    try:
        publicacion = Publicacion(id_usuario=id_usuario, contenido=contenido)
        if publicacion.guardar_publi():
            print(f'Publicacion creada')
        else:
            print(f'No se podia crear la publicacion.')

    except Exception as e:
        logging.error(f'Error al crear la publicacion: {e}')



def listar_publicaciones():
    print("\n Publicaciones")

    try:
        publicaciones = Publicacion.obtener_todos_publi()
        if not publicaciones:
            print(f'No hay publicaciones')
            return
        
        for publicacion in publicaciones:
            print(f'{publicacion.id} {publicacion.usuario_id} {publicacion.contenido} {publicacion.fecha_publi}')

    except Exception as e:
        logging.error(f'Error al listar las publicaciones: {e}')