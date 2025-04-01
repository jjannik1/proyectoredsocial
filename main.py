from database import BaseDatos
from usuario import Usuario
from publicacion import Publicacion
from dotenv import load_dotenv
import os



def menu():

    while True:


        print("\n Menu")
        print("1. Gestionar Usuario")
        print("2. Gestionar Publiaciones")
        print("3. Consultas Avanzadas")
        print("4. Salir")
