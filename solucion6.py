productos = []
class Producto:
    # Constructor de clase
    def __init__(self):
        self.codigo = ("")
        self.repuesto = ("")
        self.marca = ("")
        self.anio = ()
        #print('Se ha registrado el producto:\n',self.repuesto,"\nMarca:",self.marca,"\nAño de fabricación:",self.anio)

    #def __str__(self):
    #    return '{} {} ({})'.format(self.codigo, self.repuesto, self.marca)
    
    def buscar(self):
        buscarProd = input("Ingrese el código del producto a buscar: ").upper()
        if buscarProd == self.codigo:
            print("Producto encontrado:",self.codigo,self.repuesto,self.marca,self.anio)
        else:
            print("Producto no encontrado en el sistema.")

    def menu(self):
        while True:
            rpt = int(input("\n-------MENÚ-------\nIngrese una opción válida:\n1.Registrar producto\n2.Mostrar productos registrados\n3.Buscar productos\n4.Salir\n->Ingrese su respuesta: "))
            if rpt >4:
                print("Respuesta errónea.\nFinalizando programa")
                break
            elif rpt==1:
                #print("Registre un producto.")
                p = Producto()
                p.codigo= input("Ingrese el código del producto: ").upper()
                p.repuesto = input("Ingrese el nombre del repuesto: ").upper()
                p.marca = input("Ingrese la marca del producto: ").upper()
                p.anio = int(input("Ingrese el año de fabricación del producto: "))
                print("Producto registrado.")
                productos.append(p)
                #prodRegistrados = Catalogo()
                #prodRegistrados.productos.append(p)
            elif rpt ==2:
                #print("mostrar alumnos registrados")
                #p=Producto()
                #print(productos)
                print("\n---PRODUCTOS---")
                for p in productos:
                    print("CÓDIGO:",p.codigo,"\nNOMBRE DEL REPUESTO:",p.repuesto,"\nMARCA:",p.marca,"\nAÑO DE FABRICACIÓN:",p.anio)
            elif rpt==3:
                filtro = int(input("Ingrese el año de fabricación del producto a buscar: "))
                #print(productos)
                for filtro in productos:
                    print (p.codigo,"-",p.repuesto,"-",p.marca,"-",p.anio)
            elif rpt==4:
                print("Saliendo del programa")
                break

class Catalogo:
    #productos = [] 

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar(self, p):  
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)  # Print toma por defecto str(p)


        

#class Producto:

z = Producto()
z.menu()
