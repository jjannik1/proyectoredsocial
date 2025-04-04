import sqlite3 as base_datos
from settings import DB_FILE, CREATE_TABLES_SQL, INSERT_MULTIPLE_COLUMNS_Usuarios, INSERT_MULTIPLE_COLUMNS_Publicaciones
import logging
import os

# Configuración del logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Ruta de la base de datos
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_FILE)

class BaseDatos:
    def __init__(self):
        """
        Inicializa la conexión a la base de datos.
        Inicializa la clase con el nombre del archivo de la base de datos
        obtenido desde settings.py.
        """
        self.nombre_bd = DB_PATH

    def __enter__(self):
        """        
        Permite usar la clase como un context manager.
        Abre la conexión y crea las tablas si no existen.

        :return: Objeto conexión.
        """
        try:
            self.conexion = base_datos.connect(self.nombre_bd)
            self.cursor = self.conexion.cursor()
            logging.info("✅ Conectado a la base de datos.")
            return self  # Devuelve la instancia de BaseDatos
        except base_datos.Error as e:
            logging.error(f"❌ Error al conectar con la base de datos: {e}")
            raise e

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        """
        Cierra la conexión automáticamente al salir del bloque with,
        asegurando que los cambios se guarden.

        Método especial para cerrar la conexión al salir del Contex Manager,
        incluso si ocurre una excepción.

        :param tipo_excepcion: Tipo de excepción (si ocurre).
        :param valor_excepcion: Valor de la excepción (si ocurre).
        :param traceback: Rastreo del error (si ocurre).
        """
        try:
            if self.conexion:
                self.conexion.commit()  # Guarda los cambios
                self.cerrar_conexion()
                logging.info("✅ Conexión cerrada.")
        except base_datos.Error as e:
            logging.error(f"❌ Error al cerrar la conexión: {e}")      
    
    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        if self.conexion:
            self.conexion.close()

    def crear_tablas(self):
        """
        Crea las tablas necesarias en la base de datos si no existen.
        Usa `executescript()` para ejecutar múltiples sentencias SQL en una sola llamada.
        """
        try:
            #self.__enter__()  # Abre la conexión manualmente
            self.cursor.executescript(CREATE_TABLES_SQL)  # Ejecuta el script SQL de creación
            self.conexion.commit()
            logging.info("✅ Tablas creadas o verificadas correctamente.")
        except base_datos.Error as e:
            logging.error(f"❌ Error al crear las tablas: {e}")
            raise e  # Lanza la excepción para que sea manejada externamente
        #finally:
            #self.__exit__(None, None, None)  # Cierra la conexión manualmente
    
    def insertar_datos_iniciales(self):
        """Inserta datos iniciales en la base de datos."""
        try:
            #self.__enter__()  # Abre la conexión manualmente
            self.cursor.executemany("INSERT INTO usuarios (nombre, apellido, correo) VALUES (?, ?, ?)", INSERT_MULTIPLE_COLUMNS_Usuarios)
            self.cursor.executemany("INSERT INTO publicaciones (usuario_id, contenido) VALUES (?, ?)", INSERT_MULTIPLE_COLUMNS_Publicaciones)
            self.conexion.commit()
            logging.info("✅ Datos iniciales insertados correctamente.")
        except base_datos.Error as e:
            logging.error(f"❌ Error al insertar datos iniciales: {e}")
        #finally:
            #self.__exit__(None, None, None)  # Cierra la conexión manualmente
    
    def ejecutar_consulta(self, query, params=None, many=False):
        """Ejecuta una consulta SQL, detectando si es una sola o múltiples inserciones."""
        try:
            if params:
                if many:  
                    self.cursor.executemany(query, params)  # Múltiples registros
                else:
                    self.cursor.execute(query, params)  # Un solo registro
            else:
                self.cursor.execute(query)  # Consulta sin parámetros
            return self.cursor.fetchall()  # Devuelve los resultados
        except base_datos.Error as e:
            print(f"Error en la consulta: {e}")
            return None
        
        """
        # Ejemplo de uso con execute() (un solo registro)
        with BaseDatos("mi_base_de_datos.db") as db:
            db.ejecutar_consulta("INSERT INTO usuarios (nombre) VALUES (?)", ("Carlos",))

        Ejemplo de uso con executemany() (varios registros)
        usuarios = [("Ana",), ("Pedro",), ("Laura",)]
        with BaseDatos("mi_base_de_datos.db") as db:
            db.ejecutar_consulta("INSERT INTO usuarios (nombre) VALUES (?)", usuarios, many=True)

        """

