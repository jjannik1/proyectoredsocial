import sqlite3
from settings import DB_FILE

class BaseDatos:
    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

    def ejecutar_consulta(self,query,params=None):
        pass


    def cerrar_conexion(self):
        self.connection.close()

    