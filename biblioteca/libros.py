from utilidades import verificar_entero

libros={}

def agregar_libro():
    titulo=input("digite el titulo del libro: ").title()
    autor=input("digite el nombre del autor: ")
    cantidad=verificar_entero("cantidad")
    
    if titulo in libros:
        print(f"el libro {libros[titulo]["titulo"]} ya existe")
        agregar_libro()
    else:
        libros[titulo] = {
        "titulo":titulo,
        "autor": autor,
        "cantidad": cantidad
        }

def buscar_libro():
    while True:
        nombre_id=input("digite el nombre del libro a buscar: ").title()
        if nombre_id in libros:
            if libros[nombre_id]["cantidad"] >= 1:
                print(f"el libro se encuntra disponible con {libros[nombre_id]['cantidad']} unidades")
                break
            else:
                print("se encontro el libro pero no hay unidades disponibles")
        else:
            volver=input("desea volver a buscar el libro? (si/no): ")
            if volver == "si":
                buscar_libro()
            elif volver=="no":
                break
            
def existencia_libro():
    nombre_id=input("digite el nombre del libro a buscar: ").title()
    if nombre_id in libros:
        if libros[nombre_id]["cantidad"] >= 1:
            print("encontrado")
            return True, nombre_id
    else:
        print("libro no encontrado")
        return False, None
