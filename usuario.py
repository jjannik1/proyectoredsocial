import logging
from database import BaseDatos
from datetime import datetime
from settings import (
    USUARIO_INSERTAR, USUARIO_ACTUALIZAR_CORREO, USUARIO_ELIMINAR,
    PUBLICACIONES_ELIMINAR_POR_USUARIO, USUARIO_OBTENER_TODOS,
    USUARIO_OBTENER_POR_ID, USUARIO_BUSCAR_POR_NOMBRE, USUARIO_BUSCAR_POR_CORREO
)

class Usuario:
    """Clase que representa a un usuario en la red social."""
    
    def __init__(self, nombre=None, apellido=None, correo=None, id=None, fecha_registro=None):
        """Inicializa un objeto Usuario."""
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    """
    Uso de None en los parámetros del constructor
        El uso de None como valor predeterminado en los parámetros del constructor (__init__) proporciona varias ventajas importantes:

    1. Flexibilidad en la creación de objetos
        Permite crear instancias de Usuario de diferentes formas:

            # Crear un usuario completamente nuevo
            usuario_nuevo = Usuario(nombre="Ana", apellido="García", correo="ana@ejemplo.com")

            # Crear un objeto que representa un usuario existente (cargado desde la BD)
            usuario_existente = Usuario(id=1, nombre="Ana", apellido="García", 
                           correo="ana@ejemplo.com", fecha_registro="2025-04-01")

            # Crear un objeto parcial (para búsquedas o filtros)
            usuario_parcial = Usuario(nombre="Ana")

    2. Compatibilidad con operaciones de base de datos
        Cada operación CRUD (Crear, Leer, Actualizar, Eliminar) requiere diferentes conjuntos de datos:

        - Inserción: Necesita campos como nombre, apellido, correo
        - Consulta/Selección: Podría usar cualquier campo como filtro
        - Actualización: Requiere el ID y los campos que cambiarán
        - Eliminación: Generalmente solo necesita el ID

    3. Valores dinámicos predeterminados
        Permite establecer valores dinámicos cuando no se proporciona un valor. Por ejemplo:

        Si fecha_registro es None, se asigna automáticamente la fecha y hora actual.

    5. Distinción entre "no proporcionado" y "vacío"
        None indica claramente "no se proporcionó un valor", mientras que una cadena vacía "" o 0 son valores válidos que podrían tener significado en el contexto de la aplicación.
    """    
    
    def guardar(self):
        """Guarda un usuario en la base de datos."""
        try:
            with BaseDatos() as db:
                params = (self.nombre, self.apellido, self.correo, self.fecha_registro)
                db.ejecutar_consulta(USUARIO_INSERTAR, params)
                return True
        except Exception as e:
            logging.error(f"Error al guardar usuario: {e}")
            return False
    
    def actualizar_correo(self, nuevo_correo):
        """Actualiza el correo de un usuario existente."""
        try:
            with BaseDatos() as db:
                params = (nuevo_correo, self.id)
                db.ejecutar_consulta(USUARIO_ACTUALIZAR_CORREO, params)
                self.correo = nuevo_correo
                return True
        except Exception as e:
            logging.error(f"Error al actualizar correo: {e}")
            return False
    
    def eliminar(self):
        """Elimina un usuario y sus publicaciones de la base de datos."""
        try:
            with BaseDatos() as db:
                # Primero eliminamos sus publicaciones
                db.ejecutar_consulta(PUBLICACIONES_ELIMINAR_POR_USUARIO, (self.id,))
                
                # Luego eliminamos al usuario
                db.ejecutar_consulta(USUARIO_ELIMINAR, (self.id,))
                return True
        except Exception as e:
            logging.error(f"Error al eliminar usuario: {e}")
            return False
    
    def obtener_todos():
        """Obtiene todos los usuarios de la base de datos."""
        try:
            with BaseDatos() as db:
                resultados = db.ejecutar_consulta(USUARIO_OBTENER_TODOS)
                
                usuarios = []
                for row in resultados:
                    usuario = Usuario(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        correo=row[3],
                        fecha_registro=row[4]
                    )
                    usuarios.append(usuario)
                return usuarios
        except Exception as e:
            logging.error(f"Error al obtener usuarios: {e}")
            return []
        
    def obtener_por_id(id_usuario):
        """Obtiene un usuario por su ID."""
        try:
            with BaseDatos() as db:
                resultados = db.ejecutar_consulta(USUARIO_OBTENER_POR_ID, (id_usuario,))
                
                if resultados and len(resultados) > 0:
                    row = resultados[0]
                    return Usuario(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        correo=row[3],
                        fecha_registro=row[4]
                    )
                return None
        except Exception as e:
            logging.error(f"Error al obtener usuario por ID: {e}")
            return None    
    
    def buscar_por_nombre(nombre):
        """Busca usuarios por nombre."""
        try:
            with BaseDatos() as db:
                resultados = db.ejecutar_consulta(USUARIO_BUSCAR_POR_NOMBRE, (f"%{nombre}%",))
                
                usuarios = []
                for row in resultados:
                    usuario = Usuario(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        correo=row[3],
                        fecha_registro=row[4]
                    )
                    usuarios.append(usuario)
                return usuarios
        except Exception as e:
            logging.error(f"Error al buscar usuarios por nombre: {e}")
            return []    
    
    def buscar_por_correo(correo):
        """Busca usuarios por correo electrónico."""
        try:
            with BaseDatos() as db:
                resultados = db.ejecutar_consulta(USUARIO_BUSCAR_POR_CORREO, (f"%{correo}%",))
                
                usuarios = []
                for row in resultados:
                    usuario = Usuario(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        correo=row[3],
                        fecha_registro=row[4]
                    )
                    usuarios.append(usuario)
                return usuarios
        except Exception as e:
            logging.error(f"Error al buscar usuarios por correo: {e}")
            return []