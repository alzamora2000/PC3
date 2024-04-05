import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante 2"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante 4"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"
    
    def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return Punto(dx, dy)
    
    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        print(f"La distancia entre {self} y {otro_punto} es {distancia:.2f}")

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
    
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)
    
    def area(self):
        return self.base() * self.altura()

p1 = Punto(3, 4)
p2 = Punto(6, 8)
rectangulo = Rectangulo(p1,p2)
print("Punto 1:", p1)
print("Punto 2:", p2)
print("\nCuadrante de Punto 1:", p1.cuadrante())
print("Vector de Punto 1 a Punto 2:", p1.vector(p2))
print("\nBase del rectángulo:", rectangulo.base())
print("Altura del rectángulo:", rectangulo.altura())
print("Área del rectángulo:", rectangulo.area())
p1.distancia(p2)