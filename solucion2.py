def calificaciones():
    while True:
        try:
            #cantCalificaciones = int(input("Digite la cantidad de calificaciones que va ingresar: "))
            notas = input("Ingrese las calificaciones separandolas cada una con una coma ',': ")
            separarCalificaciones = notas.split(",")
            #print(separarCalificaciones)
            int_list = list(map(int, separarCalificaciones))
            print(int_list)
            for n in range(len(int_list)):
                n2=int_list[n]
                print("Nota N°",n+1,":",n2)
        except ValueError:
            print("Error, los valores introducidos no puedan ser convertidos debido a un error de tipeo o formato")

calificaciones()