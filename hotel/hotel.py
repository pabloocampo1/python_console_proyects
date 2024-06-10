import random
from datetime import datetime

clientes={
    12: {"nombre": "juan pablo","edad": 18,"identificacion" : 1212, "sexo": "m"}
}
habitaciones={
    "01":{
        "id":"01",
        "tipo": "normal",
        "precios": {
            "noche": 40000, 
            "hora":10000, 
            "dia": 70000},
        "camas": 2,
        "disponibilidad": True,
        },
    "02":{
        "id":"02",
        "tipo": "souit",
        "precios": {
            "noche": 120000, 
            "hora":350000, 
            "dia": 200000},
        "camas": 1,
        "disponibilidad": True,
        },
    "03":{
        "id":"03",
        "tipo": "premiun",
       "precios": {
           "noche": 50000, 
           "hora":20000, 
           "dia": 120000},
        "camas": 2,
        "disponibilidad": True,
        },
    "12":{
        "id":"12",
        "tipo": "normal",
        "precios": {
            "noche": 40000,
            "hora":10000, 
            "dia": 70000},
        "camas": 2,
        "disponibilidad": True,
        },
    "13":{
        "id":"13",
        "tipo": "normal",
        "precios": {
            "noche": 35000, 
            "hora":8000, 
            "dia": 65000},
        "camas": 1,
        "disponibilidad": True,
        },
    "14":{
        "id":"14",
        "tipo": "premiun",
        "precios": {
            "noche": 50000, 
            "hora":20000, 
            "dia": 120000},
        "camas": 1,
        "disponibilidad": True,
        },
    }
reservaciones={} 

def continuar():
    volver=input("decea salir del menu? (si/no): ")
    if volver == "si":
        return True
    elif volver == "no":
        pass
    else:
        print("dato no valido.")
        return continuar
        
        


def agregar_clientes():
    while True:
        verificacion=int(input("digite el numero de identificacion del usuario: "))
        if verificacion in clientes:
            print(f" el usuario {clientes[verificacion]["nombre"]} ya existe.")
            seguir = continuar()
            if seguir:
                break
        else:
            nombre_completop=input("nombre completo: ")
            edad=int(input("edad: "))
            identificacion=int(input("cedula: "))
            sexo=input("sexo: ")

            cliente_datos={
                "nombre": nombre_completop,
                "edad": edad,
                "identificacion" : identificacion,
                "sexo": sexo
            }
            clientes[identificacion] = cliente_datos
            print("agregado exitosamente.")
            seguir= continuar()
            if seguir:
                break

def verificar_habitacion(numero_habitacion):
    if numero_habitacion in habitaciones:
        return True
    else:
        return False
    
    
def habitaciones_disponibles():
    print("*******______habitaciones disponibles______******")
    estado=False
    for habitacion_id, detalles in habitaciones.items():
        if detalles["disponibilidad"]:
            print(f"""
                __________________________________________
                  
                - habitacion numero {habitacion_id}
                - tipo de habitacion {detalles["tipo"]}
                - numero de camas: {detalles["camas"]}
                      precios
                - por hora: {detalles["precios"]["hora"]}
                - por noche: {detalles["precios"]["noche"]}
                - por 24 horas: {detalles["precios"]["dia"]}
                      """)
            estado=True
            
    if estado == True:
        return True
    else:
        print("no hay habitaciones disponibles")
        return False
    
def datos_reservacion(habitacion):
    contador=1
    precio_total=0
    fecha1, fecha2=None, None
    for i,j in habitacion["precios"].items():
        print(f"opcion {contador}: {i} por {j}")
        contador+=1
    opcion_revervacion=int(input("Digite la opcion : "))
    
    if opcion_revervacion == 1:
        precio_total = habitacion["precios"]["noche"]
    elif opcion_revervacion == 2:
        total_horas= int(input("total de horas: "))
        precio_total= total_horas * habitacion["precios"]["hora"]
    elif opcion_revervacion == 3:
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
        fecha1 = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha2 = datetime.strptime(fecha_fin, "%Y-%m-%d")
        total= fecha2 - fecha1
        precio_total= total.days * habitacion["precios"]["dia"]
    else:
        print("opcion no valida")
        
    return precio_total, fecha1, fecha2
           

def reservar_habitacion():
    verificar_cliente=int(input("digite el numero de cedula del cliente: "))
    if verificar_cliente in clientes:
        if habitaciones_disponibles() == True:   
            opcion_habitacion=input("digite el numero de la habitacion disponible que decea: ")
            if opcion_habitacion in habitaciones and habitaciones[opcion_habitacion]["disponibilidad"] == True:
                habitaciones[opcion_habitacion]["disponibilidad"] = False
                id_reservacion=random.randint(10000, 99999)
                total_pagar, fecha_inicio, fecha_fin = datos_reservacion(habitaciones[opcion_habitacion])
                reservaciones[id_reservacion] = {}
                reservaciones[id_reservacion]["dato cliente"] = clientes[verificar_cliente]
                reservaciones[id_reservacion]["dato habitacion"] = habitaciones[opcion_habitacion]
                reservaciones[id_reservacion]["total a pagar"]= total_pagar
                reservaciones[id_reservacion]["fecha inicio"]= fecha_inicio
                reservaciones[id_reservacion]["fecha fin"]= fecha_fin
                print("se hizo la reservacion correctamente")
                print(reservaciones)
            else:
                print("hay algo mal")
    else:
        print("el usuario no esta registrado, registralo.")
        agregar_clientes()

def borrar_reservacion():
    all_reservaciones()
    id_reservacion = int(input("digite el identificador de la reserva: "))
    if id_reservacion in reservaciones:
        id_habitacion = reservaciones[id_reservacion]["dato habitacion"]["id"] 
        del reservaciones[id_reservacion] 
        habitaciones[id_habitacion]["disponibilidad"] = True  
        print("Reservación cancelada correctamente.")
    else:
        print("No se encontró esa reservación.")
        
        
def all_reservaciones():
    for clave, valor in reservaciones.items():
        print("________reservaciones______")
        print(f"reservacion {clave}")
        print(f"cliente: {valor['dato cliente']['nombre']}")
        print(f"habitacion: {valor['dato habitacion']["id"]}")
        print(f"entrada: {valor['fecha inicio']}")
        print(f"salida: {valor['fecha fin']}")
        
while True:
    print("""
          bienvenido a hotel miami
          opciones:
          1. agregar clientes
          2. hacer reservacion
          3. ver las habitaciones disponibles
          4. cancelar reservas
          5. listas todas las reservas.
          6. salir
          
          """)
    
    opcion=int(input("digite que opciones decxeas realizar: "))
    
    if opcion == 1:
        agregar_clientes()
    elif opcion == 2:
        reservar_habitacion()
    elif opcion == 3: 
        habitaciones_disponibles()
    elif opcion == 4: 
        borrar_reservacion()
    elif opcion == 5: 
        all_reservaciones() 
    elif opcion == 6: 
        print("saliendo del programa...")
        break
    else:
        print

