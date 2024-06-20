
import random
from doctores import doctores, citas_doctores
from pacientes import pacientes_DB

citas={}

def agendar_cita():
    estado=True
    while estado:
        fecha=input("fecha de cita: ")
        hora=input("digite la hora: ")
        id_cita=random.randint(10000,99999)
        
        if fecha in citas.values() and hora in citas.values() and id_cita in citas:
            print("ya hay una fecha y hora asignada")
            
        else:
            while True:
                nombre_doctor=input("digite el nombre del doctor: ")
                id_paciente=int(input("digite la identificacion del paciente: "))
                if nombre_doctor in doctores and id_paciente in pacientes_DB:
                    razon=input("razon de la cita: ")
                    citas[id_cita] = {
                        "id": id_cita,
                        "fecha": fecha,
                        "hora": hora,
                        "consultorio": "2 A",
                        "doctor": doctores[nombre_doctor]["nombre"],
                        "paciente": pacientes_DB[id_paciente],
                        "razon": razon,
                        "estado": True,
                    }
                    cita={}
                    cita[id_cita] = citas[id_cita]
                    doctores[nombre_doctor]["citas_pendientes"].append(cita) 
                    print("se agrego la cita correctamente")
                    estado=False
                    print(doctores)
                    break
                else:
                    print("dato invaliod, vuelve a intentarlo.")
    
def eliminar_citas():
    citas_doctores()
    id_cita = int(input("Digite el número de la cita: "))
    if id_cita in citas:
        # Elimina la cita del diccionario de citas
        """ del citas[id_cita]
        print(f"La cita con ID {id_cita} ha sido eliminada del sistema de citas.") """

        # También eliminamos la cita del registro de citas pendientes del doctor
        for doctor in doctores:
            for j in doctor.values():
                print(j)
            
    else:
        print("La cita con ese ID no existe.")
            
def listar_citas():
    print(citas)
    for i,j in citas.items():
        print("     _____________________________")
        print(f"""
            id cita {i} -- fecha: {j['fecha']} hora: {j['hora']} -- doctor: {j['doctor']} nombre paciente {j['paciente']['nombre']}
            """)