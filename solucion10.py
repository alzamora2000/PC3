import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def calcular_area_circulo():
    radio = float(input("\nIngrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print("El área del círculo es:", round(area,2))

def calcular_area_rectangulo():
    base = float(input("\nIngrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    rectangulo = Rectangulo(base, altura)
    area = rectangulo.calcular_area()
    print("El área del rectángulo es:", round(area,2))

def calcular_area_cuadrado():
    lado = float(input("\nIngrese el lado del cuadrado: "))
    area = lado ** 2
    print("El área del cuadrado es:", round(area,2))

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
