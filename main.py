# -*- coding: utf-8 -*-
from database import BaseDatos, DB_PATH
import modulos.usuarios
import modulos.publicaciones
#import modulos.consultas
import logging
import os

# Configuración del logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def inicializar_bd():
    """Crea las tablas e inserta los datos iniciales."""
    db_path = "red_social.db"  # Ruta del archivo de la base de datos
    if not os.path.exists(DB_PATH):
        print("ℹ️ La base de datos no existe. Creándola...")
        try:
            with BaseDatos() as db:
                db.crear_tablas()
                db.insertar_datos_iniciales()
        except Exception as e:
            logging.error(f"Error al inicializar la base de datos: {e}")
            print("❌ Ocurrió un error al inicializar la base de datos.")
    else:
        print("ℹ️ La base de datos ya existe. Verificando tablas...")
        try:
            with BaseDatos() as db:
                db.crear_tablas()                
        except Exception as e:
            logging.error(f"Error al inicializar la base de datos: {e}")
            print("❌ Ocurrió un error al inicializar la base de datos.")
    
def menu_usuarios():
    """Menú para gestionar usuarios."""
    #print("🔹 Gestión de Usuarios (Próximamente)")
    modulos.usuarios.mostrar_menu()

def menu_publicaciones():
    """Menú para gestionar publicaciones."""
    #print("🔹 Gestión de Publicaciones (Próximamente)")
    modulos.publicaciones.mostrar_menu()

def menu_consultas():
    """Menú para realizar consultas avanzadas."""
    print("🔹 Consultas Avanzadas (Próximamente)")
    #menus.consultas.mostrar_menu()

def menu():
    """Muestra el menú principal."""
    while True:
        print("\n📢 MENÚ PRINCIPAL")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Publicaciones")
        print("3. Consultas Avanzadas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_publicaciones()
        elif opcion == "3":
            menu_consultas()
        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":   
   inicializar_bd()
   menu()