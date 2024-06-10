
#funcionalida para que agregen una edad correcta.
def agregar_edad():
    while True:
        try:
            edad=input("edad: ")
            if not edad.isdigit():
                raise ValueError("Debes ingresar un número entero para la edad.")
            edad = int(edad)
            if edad <= 1 or edad > 100:
               raise ValueError("edad no valida")
            return edad
        except ValueError as e:
            print("error", e)

#verificar si un dato ingresado si es entero
def verificar_entero(dato):
    while True:
        try:
            dato=int(input(f"digite {dato}: "))
            return dato
        except ValueError:
                print("errorr debes agregar un dato tipo entero")