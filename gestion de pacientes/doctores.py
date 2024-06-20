
doctores={
    "Juan alberto":{
        "nombre": "Juan alberto", 
        "especialidad": "Cirujano",
        "citas_pendientes": []
    },
    "Mariana rojas":{
        "nombre": "Mariana rojas", 
        "especialidad": "Medico general",
        "citas_pendientes": {}
    },
    "Maria":{
        "nombre": "Maria", 
        "especialidad": "dentista",
        "citas_pendientes": {}
    },
}


def citas_doctores():
    id_doctor=input("digite el nombre del doctor: ")
    if id_doctor in doctores:
        for i, j in doctores.items():
            print(i, j["citas_pendientes"])