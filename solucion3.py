from math import pi

try:
    class Circulo():
        def __init__(self):
            self.radio = int(input("Ingrese el radio del círculo:\n-> "))
            area = pi*self.radio**2
            print(f"El área del círculo es: {round(area,2)}")
except ValueError:
    print("Los datos ingresados no son numéricos.")

Circulo()