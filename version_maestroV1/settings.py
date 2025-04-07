import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Nombre del archivo de base de datos
#DB_FILE = os.getenv("DB", "sistema.db")

DB_FILE = os.getenv("DB")
if not DB_FILE:
    raise ValueError("❌ Error: La variable de entorno DB no está definida.")


# Script para crear la tabla de clientes si no existe
CREATE_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS usuarios (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   nombre TEXT NOT NULL,
   apellido TEXT NOT NULL,
   correo TEXT UNIQUE NOT NULL,
   fecha_registro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS publicaciones (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   usuario_id INTEGER NOT NULL,
   contenido TEXT NOT NULL,
   fecha_publicacion DATE DEFAULT CURRENT_DATE,
   FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
"""

# Datos iniciales
INSERT_MULTIPLE_COLUMNS_Usuarios = [
  ("Leonardo", "Caballero", "leonardo@mail.com"),
  ("Ana", "Poleo", "ana@mail.com"),
  ("Manuel", "Matos", "manuel@mail.com"),
]

INSERT_MULTIPLE_COLUMNS_Publicaciones = [
  (1, "Mi primera publicación en la red social"),
  (2, "¡Hola a todos!"),
  (3, "Estoy aprendiendo Python y SQLite"),
]