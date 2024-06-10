""" Ejercicio 3: Sistema de Gestión de Bibliotecas
Descripción:
Una biblioteca necesita un sistema para gestionar los préstamos de libros. El sistema 
debe permitir registrar 
libros, usuarios y gestionar los préstamos.

Requisitos:
Una función para registrar nuevos libros con título, autor y cantidad disponible.
Una función para registrar nuevos usuarios.
Una función para prestar libros a usuarios.
Una función para devolver libros.
Una función para listar todos los préstamos actuales.
 y otros mas
"""


#modulos 
from clientes import agregar_clientes, mostrar_info
from libros import agregar_libro, buscar_libro
from prestamos import hacer_prestamo, devolver_prestamo, mostrar_prestamos

while True:
    print("""
    *******biblioteca jupa*****
    
                MENU
                
    1. Agregar un nuevo usuario - v
    2. buscar usuario - v
    3. Agregar libro - v
    4. Buscar libros - v
    5. Prestar libro
    6. Devolver libros
    7. Listar todos los prestamos
    8. Salir del sistema
        
    """)
    opcion_menu=int(input("Digite el numero de la opcion: "))
    
    if opcion_menu == 1:
        agregar_clientes()
        while True:
            volver=input("agregar otro usuario? (si/no): ")
            if volver == "si":
                agregar_clientes()
            elif volver == "no":
                break
            else:
                print("dato no valido.")
            
    elif opcion_menu == 2:
        mostrar_info()
    elif opcion_menu == 3:
        agregar_libro()
    elif opcion_menu == 4:
        buscar_libro()
    elif opcion_menu == 5:
        hacer_prestamo()
    elif opcion_menu == 6:
        devolver_prestamo()
    elif opcion_menu == 7:
        mostrar_prestamos()
    elif opcion_menu == 8:
        print("saliendo del sistema...")
        break
    else:
        print("opcion no valida.")
        
    # hacer las demas opciones    
            
        
