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
    print

def editar_paciente():
    print


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