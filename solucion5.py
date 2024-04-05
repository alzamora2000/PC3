lista = list()
class Alumno:
    def __init__(self):
        self.numRegistro = ()
        self.nombre = ("")
        self.edad = ()
        self.nota = ()
        #self.nombre = input("Ingrese el nombre del alumno a registrar: ")
        #self.numRegistro = int(input("Ingrese el N° de registro del alumno: "))
    def menu(self):
        #print("\nIngrese una opción válida:\n1.Display(Información del estudiante)\n2.SetAge(Asinga la edad del estudiante)\n3.SetNota(Asigna la nota del estudiante)\n-> ")
        #rpt=0
        #rpt = int(input("\nIngrese una opción válida:\n1.Display(Información del estudiante)\n2.SetAge(Asinga la edad del estudiante)\n3.SetNota(Asigna la nota del estudiante)\n-> "))
        while True:
            rpt = int(input("\n-------MENÚ-------\nIngrese una opción válida:\n1.Registrar un alumno\n2.Mostrar alumnos registrados\n3.Salir\n->Ingrese su respuesta: "))
            if rpt >3:
                print("Respuesta errónea.\nFinalizando programa")
                break
            elif rpt==1:
                #print("Registre un alumno.")
                Alumno.registrar(self)
            elif rpt ==2:
                #print("mostrar alumnos registrados")
                Alumno.mostrar(self)  
            elif rpt==3:
                print("Saliendo del programa.")
                break
    def registrar(self):
        print("Función registrar:")
        alumno = Alumno()
        alumno.numRegistro = int(input("Introduce el N° de registro: "))
        alumno.nombre = input("Ingrese el nombre del alumno: ")
        alumno.edad = int(input("Ingrese edad del alumno: "))
        alumno.nota = int(input("Ingrese la nota del alumno: "))
        print("\n¡Alumno registrado correctamente!")
        lista.append(alumno)
    def mostrar(self):
        print("\n---Lista de alumnos---\n")
        for alumno in lista:
            print("Registro N°",alumno.numRegistro,"\nNombre:",alumno.nombre,"\nEdad:",alumno.edad,"\nNota:",alumno.nota,"\n")

datos = Alumno()
datos.menu()

