from utilidades import agregar_edad, verificar_entero


clientes_db={}

def agregar_clientes():
    nombre=input("nombre: ")
    edad= agregar_edad()
    identificacion=verificar_entero("identificacion")
    direccion=input("direccion: ")
    telefono=verificar_entero("telefono")
    
    
    if identificacion in clientes_db:
        print("numero de identificacion no valido, ya hay un usuario con esa identificacion.")
        agregar_clientes()
    else:
        clientes_db[identificacion] = {
            "nombre":nombre,
            "edad": edad ,
            "identificacion":identificacion,
            "direccion":direccion,
            "telefono":telefono,
            "total de prestamos": 0,
            "prestamos":{},
        }
        
    
    
def mostrar_info():
    identificador=verificar_entero("identificacion")
    
    if identificador in clientes_db:
        print("usuario encontrado.")
        for i, j in clientes_db[identificador].items():
            print(f"{i} {j}")
    else:
        print("usuario no encontrado, vuelve a intentarlo.")
        mostrar_info()        
        
def buscar_cliente():
    identificacion=verificar_entero("identificacion")
    if identificacion in clientes_db:
        return True, identificacion
    else:
        return False, None
    
