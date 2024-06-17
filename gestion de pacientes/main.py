""" Ejercicio 6: Sistema de Gestión de Pacientes
Descripción:
Una clínica necesita un sistema para gestionar la información de sus pacientes,
citas médicas y tratamientos.

Requisitos:
Una función para registrar nuevos pacientes con su información personal y médica.
Una función para agendar citas médicas.
Una función para registrar tratamientos y su progreso.
Una función para listar las citas de un paciente.
Una función para listar todos los pacientes. """

from pacientes import agregar_pacientes, eliminar_paciente, editar_paciente

def menu():
    print("""
        menu
        1. gestion de pacientes 
        2. gestion de citas
        3. gestion de tratamiento
        4. salir
        """)
    opcion=int(input("digite la opcion que decea realizar"))
    if opcion == " " or opcion > 4 and opcion < 1:
        print("opcion no valida")
        menu()
    elif opcion == 1:
        menu_pacientes()
    elif opcion == 2:
        print
    elif opcion == 3:
        print
    elif opcion == 4:
        print
    elif opcion == 5:
        print


def menu_pacientes():
    print("""
        menu - pacientes
        1. agregar paciente
        2. eliminar paciente
        3. editar datos de un paciente
        4. salir al menu principal
        """)
    while True:
        opcion_paciente=int(input("digite la opcion que decea: "))
        if opcion_paciente == 1:
            agregar_pacientes()
        elif opcion_paciente == 2:
            eliminar_paciente()
        elif opcion_paciente == 3:
            editar_paciente()
        elif opcion_paciente == 4:
            return menu()  
        else:
            print("dato no valido")
            

if __name__ == "__main__":
    menu()