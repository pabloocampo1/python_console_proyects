from libros import libros, existencia_libro
from clientes import clientes_db, buscar_cliente
import random
prestamos={}

def hacer_prestamo():
    esta_cliente,  id_cliente = buscar_cliente()
    esta_libro, id_libro = existencia_libro()
    
    if esta_cliente :
        if esta_libro:
            while True:
                id_prestamo=random.randint(10000, 99999)
                fecha_prestamo=input("fecha prestamos: ")
                fecha_entrega=input("fecha de entrega: ")
                confirmar_prestamo=input("decea confirmar el prestamo?(si/no): ")
                if confirmar_prestamo == "si":
                    #agregarlo a los usuarios
                    libros[id_libro]["cantidad"] -= 1
                    clientes_db[id_cliente]["total de prestamos"] += 1
                    clientes_db[id_cliente]["prestamos"][id_prestamo] = {
                        "fecha de prestamo": fecha_prestamo,
                        "fecha de entrega": fecha_entrega,
                        "libro": libros[id_libro]["titulo"],
                    }
                    #agregarlo a los prestamos
                    prestamos[id_prestamo] = {
                        "usuario": clientes_db[id_cliente]["nombre"],
                        "libro": libros[id_libro]["titulo"],
                        "fecha de prestamo": fecha_prestamo,
                        "fecha de entrega": fecha_entrega,
                    }
                    break
                elif confirmar_prestamo == "no":
                    break
    else:
        print("algun dato no valido")
        
        
def devolver_prestamo():
    esta_cliente, id_cliente = buscar_cliente()
    
    if esta_cliente:
        print(f"prestamos del cliente")
        for i, j in clientes_db[id_cliente]["prestamos"].items():
            print(f"{i} : {j}")
        id_libro=input("digite el nombre del libro a entregar: ").title()
        if id_libro in libros:
            id_prestamo=int(input("digite el id del prestamo: "))
            libros[id_libro]["cantidad"] += 1
            del clientes_db[id_cliente]["prestamos"][id_prestamo]
            #eliminar en a BD de libros
            del prestamos[id_prestamo]
            print("se entrego correctamente")
        else:
            print("no se encontro el libro")
            
            
def mostrar_prestamos():
    if len(prestamos) < 1:
        print("_____________no hay prestamos__________")
    else:
        for  i, j in prestamos.items():
            print("   __________________") 
            print(f"""
                numero de prestamo {i}
                usuario: {j['usuario']}
                libro_ {j['libro']}
                fecha de prestamo {j['fecha de prestamo']}
                fecha de entrega {j['fecha de entrega']}
                
                
                """)