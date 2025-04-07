from database import BaseDatos
from settings import *
import logging
from datetime import datetime

class Publicacion:
    def __init__(self,id=None,id_usuario=None,contenido=None,fecha_publi=None):
        self.id = id
        self.id_usuario = id_usuario
        self.contenido=contenido
        self.fecha_publi = fecha_publi or datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def guardar_publi(self):
        try:
            with BaseDatos() as db:
                params = (self.id_usuario, self.contenido, self.fecha_publi)
                db.ejecutar_consulta(PUBLICACIONES_INSERT, params)
                return True
        except Exception as e:
            logging.error(f'Error al guardar publicacion: {e}')
            return False
        
    
    def obtener_todos_publi():
        try:
            with BaseDatos() as db:
                resultado = db.ejecutar_consulta(PUBLICACIONES_OBTENER_TODOS)

                publicaciones = []
                for i in resultado:
                    publicacion = Publicacion(id=i[0], id_usuario=i[1], contenido=i[2], fecha_publi=i[3])
                    publicaciones.append(publicacion)
                return publicaciones
            
        except Exception as e:
            logging.error(f'Error al obtener las publicaciones: {e}')
            return []
        

    def obtener_publi_por_usuario(id_usuario):
        try:
            with BaseDatos() as db:
                resultados = db.ejecutar_consulta(PUBLICACIONES_POR_USUARIO, (id_usuario,))

                publicaciones = []
                for i in resultados:
                    publicacion = Publicacion(
                        id=i[0],
                        id_usuario=i[1],
                        contenido=i[2],
                        fecha_publi=i[3]
                    )
                    publicaciones.append(publicacion)


                return publicaciones

        except Exception as e:
            logging.error(f'Error al obtener las publicaciones: {e}')
            return []
        


    def editar_contenido(self, contenido_nuevo):
        try:
            with BaseDatos() as db:
                params = (contenido_nuevo, self.id)
                db.ejecutar_consulta(PUBLICACION_ACTUALIZAR_CONTENIDO, params)
                self.contenido = contenido_nuevo
                return True
        except Exception as e:
            logging.error(f'Error al actualizar el contenido: {e}')
            return False
        
    def eliminar_publicacion(self):
        try:
            with BaseDatos() as db:
                db.ejecutar_consulta(PUBLICACIONES_ELIMINAR_POR_USUARIO, (self.id,))
                return True
            
        except Exception as e:
            logging.error(f'Error al eliminar la publicacion: {e}')
            return False
        


    def obtener_por_id(id_publicacion):

        try:
            with BaseDatos() as db:
                resultados = db.ejecutar_consulta(PUBLICACION_OBTENER_POR_ID, (id_publicacion,))

                if resultados and len(resultados) > 0:
                    row = resultados[0]
                    return Publicacion(id=row[0],
                                       id_usuario=row[1],
                                       contenido=row[2],
                                       fecha_publi=row[3]
                                       )
                return None
            
        except Exception as e:
            logging.error(f'Error al obtener publicacion por ID: {e}')
            return None