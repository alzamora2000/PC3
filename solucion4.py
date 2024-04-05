try:
    class Rectangulo:
        def __init__(self):
            self.largo = int(input("Ingrese el largo: "))
            self.ancho=int(input("Ingrese el ancho: "))
        def area(self):
            area=self.largo * self.ancho
            print("El área del rectángulo es:",area)
except ValueError:
    print("Los datos ingresados no son numéricos.")


respuesta = Rectangulo()
respuesta.area()



