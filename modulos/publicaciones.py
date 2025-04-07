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

        elif opcion == "3":
            listar_publicacion_por_usuario()

        elif opcion == "4":
            editar_contenido()
        
        elif opcion == "5":
            eliminar_publicacion()

        elif opcion == "6":
            print("Volviendo al menu principal")
            break

        else:
            print("Opcion invalida. Intente de nuevo.")





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
            print(f'{publicacion.id} {publicacion.id_usuario} {publicacion.contenido} {publicacion.fecha_publi}')

    except Exception as e:
        logging.error(f'Error al listar las publicaciones: {e}')



def listar_publicacion_por_usuario():
    print("\n Publicacion por usuario")

    try:
        usuario = int(input("Introduce el ID del usuario: "))
        publicacion = Publicacion.obtener_publi_por_usuario(usuario)
        
        for i in publicacion:
            print(f'{i.id} {i.id_usuario} {i.contenido} {i.fecha_publi}')


    
    except Exception as e:
        logging.error(f'Error al listar las publicaciones: {e}')


def editar_contenido():
    print("\n Edicion de contenido")

    try:
        id_publicacion = input("Introduce el ID de la publicacion: ")
        publicacion = Publicacion.obtener_por_id(int(id_publicacion))
        if not publicacion:
            print(f'No existe una publicacion con ID {id_publicacion}')
            return
        
        print(f'Contenido: {publicacion.contenido}')

        content = input("Nuevo contenido: ")

        if publicacion.editar_contenido(content):
            print("Contenido actualizado correctamente.")

        else:
            print("No se podia actualizar el contenido")

    except Exception as e:
        logging.error(f'Error al editar el contenido: {e}')



def eliminar_publicacion():
    """Elimina una publicacion"""
    print("\n ELIMINAR PUBLICACION")
    id_publicacion = input("ID de la publicacion a eliminar: ")
    if not id_publicacion.isdigit():
        print("El ID debe ser un numero.")
        return
    
    try:
        publicacion = Publicacion.obtener_por_id(int(id_publicacion))
        if not publicacion:
            print(f"No existe una publicacion con ID {id_publicacion}.")
            return
        
        print(f'ID: {publicacion.id} ID de Usuario {publicacion.id_usuario}')
        print(f'Contenido: {publicacion.contenido}')
        print(f'Fecha de publicacion: {publicacion.fecha_publi}')
        print("\n ADVERTENCIA: Esto elimina la publicacion definitivamente")
        confirmacion = input("¿Estas seguro de eliminar esta publicacion? (s/n): ").lower()

        if confirmacion == "s":
            if publicacion.eliminar_publicacion():
                print("Publicacion eliminado correctamente")
            else:
                print("No se pudo eliminar la publicacion.")
                
        else:
            print("Operacion cancelada.")

    except Exception as e:
        logging.error(f'Error al eliminar publicacion: {e}')
