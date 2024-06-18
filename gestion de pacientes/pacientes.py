from utilidades import seguir

pacientes_DB={
    212242 : {
        "nombre": "juan",
        "edad": 23,
        "cedula": 212242,
        "direccion": "fsfs",
        "telefono": 32232342,
    }    
}


def agregar_pacientes():
    nombre=input("nombre: ")
    edad=verificar_edad()
    identificacion= verificar_cedula()
    direccion=input("direccion: ")
    telefono=int(input("telefono: "))

    pacientes_DB[identificacion] = {
        "nombre": nombre,
        "edad": edad,
        "cedula": identificacion,
        "direccion": direccion,
        "telefono": telefono,
    }
    
    if verificar_existencia(identificacion):
        print(f"el usuario {pacientes_DB[identificacion]["nombre"]} fue agregado correctamente ")
    else:
        print("el usuario no se pudo registrar")

def eliminar_paciente():
    intentos=0
    while intentos <= 3:
        if intentos == 3:
            volver=input("ya lo has intentado tres veces, deceas salir al menu? (si/no): ").lower()
            if volver == "si":
                break
            elif volver == "no":
                intentos=0
            else:
                print("dato incorrecto. ")
        id_paciente=int(input("digite el numero de identificacion del usuario a eliminar: "))
        if id_paciente in pacientes_DB:
            validar_eliminacion=input(f"se encontro el usuario {pacientes_DB[id_paciente]["nombre"]}, seguro que deceas eliminarlo? (si/no): ").lower()
            if validar_eliminacion == "si":
                del pacientes_DB[id_paciente]
                estado = verificar_existencia(id_paciente)
                if estado:
                    print("no se puedo eliminar el paciente")
                    intentos+=1
                else:
                    print("se elimino correctamente.")
                    break
            elif validar_eliminacion=="no":
                break
            else:
                print("informacion invalida")
                intentos+=1
        else:
            print(f"No se encontro el usuario con identificacion {id_paciente}")
            intentos+=1   

def editar_paciente():
    id_paciente=int(input("digite la identificacion del paciente: "))
    if verificar_existencia(id_paciente):
        while True:
            print("""
            que datos decea editar?
            1. nombre
            2. edad
            3. direccion
            4. telefono
            """)
            opcion=int(input("digite que opcion decea realizar: "))
            if opcion == 1:
                nombre_nuevo=input("digite el nuevo nombre: ").title()
                nombre_anterior=pacientes_DB[id_paciente]["nombre"]
                pacientes_DB[id_paciente]["nombre"] = nombre_nuevo
                if verficar_igualdad(nombre_nuevo,nombre_anterior ):
                    print("actualizado correctamente")
                    if seguir("editando datos"):
                        pass
                    else:
                        break
                else:
                    print("no se pudo actualizar correctamente, intentalo de nuevo.")
                    editar_paciente()
            elif opcion == 2:
                edad_nuevo=int(input("digite la nuevo edad: "))
                edad_anterior=pacientes_DB[id_paciente]["edad"]
                pacientes_DB[id_paciente]["edad"] = edad_nuevo
                if verficar_igualdad(edad_nuevo, edad_anterior ):
                    print("actualizado correctamente")
                    if seguir("editando datos"):
                        pass
                    else:
                        break
                else:
                    print("no se pudo actualizar correctamente, intentalo de nuevo.")
                    editar_paciente()
            elif opcion == 3:
                nueva_direccion=input("digite la nueva direccion: ")
                direccion_vieja=pacientes_DB[id_paciente]["direccion"]
                pacientes_DB[id_paciente]["direccion"] = nueva_direccion
                if verficar_igualdad(nueva_direccion, direccion_vieja ):
                    print("actualizado correctamente")
                    if seguir("editando datos"):
                        pass
                    else:
                        break
                else:
                    print("no se pudo actualizar correctamente, intentalo de nuevo.")
                    editar_paciente()
            elif opcion == 4:
                nuevo_telefono=int(input("digite el nuevo telefono: "))
                telefono_viejo=pacientes_DB[id_paciente]["telefono"]
                pacientes_DB[id_paciente]["telefono"] = nuevo_telefono
                if verficar_igualdad(nuevo_telefono, telefono_viejo ):
                    print("actualizado correctamente")
                    if seguir("editando datos"):
                        pass
                    else:
                        break
                else:
                    print("no se pudo actualizar correctamente, intentalo de nuevo.")
                    editar_paciente()
            else:
                print("dato invalido")


def ver_pacientes():
    print("_______pacientes___________")
    for i, j in pacientes_DB.items():
        print("---------------------------------------------------------------------------------------")
        print(f"id paciente {i} nombre {j['nombre']} edad {j['edad']} numero telefono {j['telefono']}")


def verificar_edad():
    while True:
        try:
            edad=int(input("edad: "))
            if edad >= 120 or edad <= 0:
                raise ValueError("edad no valida")
            else:
                return edad
        except ValueError as e:
            print(e)

def verificar_cedula():
    while True:
        try:
            identicacion=int(input("identificacion: "))
            identicacion = str(identicacion)
            if identicacion in pacientes_DB:
                raise ValueError("estas ingresando una identificacion que ya esta en el sistema.")
            elif len(identicacion) <= 5 or len(identicacion) > 10:
                raise ValueError("estas ingresando una identicacion muy larga o corta")
            else:
                return int(identicacion)
        except ValueError as e:
            print(e)
            
def verificar_existencia(id):
    if id in pacientes_DB:
        return True
    else:
        return False

def verficar_igualdad(item_ingresado, item_DB):
    if item_ingresado != item_DB:
        return True
    else:
        return False