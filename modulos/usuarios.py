import logging
from usuario import Usuario

"""
Este módulo tiene las siguientes características:

- Menú completo para gestionar usuarios con 6 opciones.
- Validaciones básicas de entrada (verificando IDs numéricos, campos obligatorios, formato de correo).
- Proporciona mensajes claros con emojis para una mejor experiencia de usuario.
- Maneja errores de forma robusta, mostrando mensajes amigables y registrando detalles.
- Requiere confirmación para acciones destructivas como eliminar usuarios.
- Presenta datos tabulados para mejor legibilidad.
- Separa la lógica de presentación (interfaz) de la lógica de negocio (clase Usuario).
"""

def mostrar_menu():
    """Menú para gestionar usuarios."""
    while True:
        print("\n🔹 GESTIÓN DE USUARIOS")
        print("1. Registrar nuevo usuario")
        print("2. Listar todos los usuarios")
        print("3. Buscar usuario")
        print("4. Actualizar correo de usuario")
        print("5. Eliminar usuario")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            actualizar_correo_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            print("👋 Volviendo al menú principal...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

def registrar_usuario():
    """Registra un nuevo usuario en la base de datos."""
    print("\n📝 REGISTRAR NUEVO USUARIO")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo electrónico: ")
    
    # Validación básica
    if not nombre or not apellido or not correo:
        print("❌ Todos los campos son obligatorios.")
        return
    
    if '@' not in correo:
        print("❌ El correo electrónico no es válido.")
        return
    
    try:
        usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo)
        if usuario.guardar():
            print(f"✅ Usuario {nombre} {apellido} registrado correctamente.")
        else:
            print("❌ No se pudo registrar el usuario.")
    except Exception as e:
        print(f"❌ Error al registrar usuario: {e}")
        logging.error(f"Error al registrar usuario: {e}")

def listar_usuarios():
    """Lista todos los usuarios registrados."""
    print("\n📋 LISTA DE USUARIOS")
    try:
        usuarios = Usuario.obtener_todos()
        if not usuarios:
            print("ℹ️ No hay usuarios registrados.")
            return
        
        print(f"{'ID':<5} {'NOMBRE':<15} {'APELLIDO':<15} {'CORREO':<25} {'FECHA REGISTRO':<20}")
        print("-" * 80)
        for usuario in usuarios:
            print(f"{usuario.id:<5} {usuario.nombre:<15} {usuario.apellido:<15} {usuario.correo:<25} {usuario.fecha_registro:<20}")
    except Exception as e:
        print(f"❌ Error al listar usuarios: {e}")
        logging.error(f"Error al listar usuarios: {e}")

def buscar_usuario():
    """Busca un usuario por nombre o correo electrónico."""
    print("\n🔍 BUSCAR USUARIO")
    print("1. Buscar por nombre")
    print("2. Buscar por correo")
    opcion = input("Seleccione una opción: ")
    
    try:
        if opcion == "1":
            termino = input("Ingrese el nombre a buscar: ")
            usuarios = Usuario.buscar_por_nombre(termino)
        elif opcion == "2":
            termino = input("Ingrese el correo a buscar: ")
            usuarios = Usuario.buscar_por_correo(termino)
        else:
            print("❌ Opción inválida.")
            return
        
        if not usuarios:
            print(f"ℹ️ No se encontraron usuarios con el término '{termino}'.")
            return
        
        print(f"{'ID':<5} {'NOMBRE':<15} {'APELLIDO':<15} {'CORREO':<25} {'FECHA REGISTRO':<20}")
        print("-" * 80)
        for usuario in usuarios:
            print(f"{usuario.id:<5} {usuario.nombre:<15} {usuario.apellido:<15} {usuario.correo:<25} {usuario.fecha_registro:<20}")
    except Exception as e:
        print(f"❌ Error al buscar usuarios: {e}")
        logging.error(f"Error al buscar usuarios: {e}")

def actualizar_correo_usuario():
    """Actualiza el correo de un usuario."""
    print("\n✏️ ACTUALIZAR CORREO DE USUARIO")
    id_usuario = input("ID del usuario: ")
    if not id_usuario.isdigit():
        print("❌ El ID debe ser un número.")
        return
    
    try:
        usuario = Usuario.obtener_por_id(int(id_usuario))
        if not usuario:
            print(f"❌ No existe un usuario con ID {id_usuario}.")
            return
        
        print(f"Usuario: {usuario.nombre} {usuario.apellido}")
        print(f"Correo actual: {usuario.correo}")
        nuevo_correo = input("Nuevo correo: ")
        
        # Validación básica del nuevo correo
        if not nuevo_correo or '@' not in nuevo_correo:
            print("❌ El correo electrónico no es válido.")
            return
            
        if usuario.actualizar_correo(nuevo_correo):
            print("✅ Correo actualizado correctamente.")
        else:
            print("❌ No se pudo actualizar el correo.")
    except Exception as e:
        print(f"❌ Error al actualizar correo: {e}")
        logging.error(f"Error al actualizar correo: {e}")

def eliminar_usuario():
    """Elimina un usuario y sus publicaciones."""
    print("\n🗑️ ELIMINAR USUARIO")
    id_usuario = input("ID del usuario a eliminar: ")
    if not id_usuario.isdigit():
        print("❌ El ID debe ser un número.")
        return
    
    try:
        usuario = Usuario.obtener_por_id(int(id_usuario))
        if not usuario:
            print(f"❌ No existe un usuario con ID {id_usuario}.")
            return
        
        print(f"Usuario: {usuario.nombre} {usuario.apellido}")
        print(f"Correo: {usuario.correo}")
        print(f"Fecha de registro: {usuario.fecha_registro}")
        print("\n⚠️ ADVERTENCIA: Esta acción eliminará el usuario y todas sus publicaciones.")
        confirmacion = input("¿Está seguro de eliminar este usuario? (s/n): ").lower()
        
        if confirmacion == 's':
            if usuario.eliminar():
                print("✅ Usuario eliminado correctamente junto con sus publicaciones.")
            else:
                print("❌ No se pudo eliminar el usuario.")
        else:
            print("ℹ️ Operación cancelada.")
    except Exception as e:
        print(f"❌ Error al eliminar usuario: {e}")
        logging.error(f"Error al eliminar usuario: {e}")