import logging
from settings import USUARIOS_ULTIMO_MES, CANTIDAD_PUBLICACIONES, USUARIOS_PUBLICAN_MAS_VECES, PUBLICACIONES_ANTIGUAS, BUSCAR_PUBLICACION
from database import BaseDatos

def mostrar_menu():
    while True:
        print("\n Consultas")
        print("1. Usuarios registrados en el último mes")
        print("2. Cantidad total de publicaciones por usuario")
        print("3. Usuarios que han publicado más de 3 veces")
        print("4. Mostrar las publicaciones más antiguas")
        print("5. Buscar publicaciones que contengan una palabra clave.")
        print("6. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            usuarios_registrados()

        elif opcion == "2":
            cantidad_publicaciones()

        elif opcion == "3":
            usuarios_publican_veces()

        elif opcion == "4":
            publicacion_antigua()

        elif opcion == "5":
            buscar_publicacion()

        elif opcion == "6":
            break

        else:
            print("Opcion invalida.")

    


def usuarios_registrados():
    try:
        with BaseDatos() as db:
            result = db.ejecutar_consulta(USUARIOS_ULTIMO_MES)

        if result:

            print(f'\n Usuarios registrados desde el ultimo mes:\n')

            for i in result:
                print(f'{i}')

        else:
            print("No existen usuarios registrados desde el ultimo mes.")

    except Exception as e:
        logging.error(f'Fallo de la consulta: {e}')


def cantidad_publicaciones():
    try:
        with BaseDatos() as db:
            result = db.ejecutar_consulta(CANTIDAD_PUBLICACIONES)

        if result:

            for i,j in result:
                print(f'ID usuario: {i} Cantidad de publicaciones: {j}')

        else:
            print("No existen usuarios que han publicado algo.")

    except Exception as e:
        logging.error(f'Fallo de la consulta: {e}')

def usuarios_publican_veces():
    try:
        with BaseDatos() as db:
            result = db.ejecutar_consulta(USUARIOS_PUBLICAN_MAS_VECES)

        if result:

            print(f'Usuarios que publican más de 3 veces')

            for i in result:
                print(f'ID usuario: {i}')

        else:
            print("No existen usuarios que han publicado mas de 3 veces")
    
    except Exception as e:
        logging.error(f'Fallo de la consulta: {e}')

def publicacion_antigua():
    try:
        with BaseDatos() as db:
            result = db.ejecutar_consulta(PUBLICACIONES_ANTIGUAS)

        if result:

            print(f'\n Publicaciones más antiguas:')

            for i in result:
                print(f'\n {i}')

        else:
            print("No existen publicaciones.")

    except Exception as e:
        logging.error(f'Fallo de la consulta: {e}')


def buscar_publicacion():
    try:
        palabra_clave = input("Introduce una palabra que contenga una publicación: ")

        palabra_clave = "%"+palabra_clave+"%"
        with BaseDatos() as db:
            result = db.ejecutar_consulta(BUSCAR_PUBLICACION, (palabra_clave,))

        if result:

            for i in result:
                print(f'\n{i}')

        else:
            print("No existen publicaciones que contengan la palabra.")

        

    except Exception as e:
        logging.error(f'Fallo de la consulta: {e}')