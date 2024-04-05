def sol1():
    while True:
        try:
            num = input("Ingrese dos números enteros en formato x/y\n -> ")

            #diferenciamos los números ingresados mediante el "/"
            resultado = num.split("/")
            #print(resultado)

            #pasamos la lista de string ingresada por teclado a int
            int_list = list(map(int, resultado))
            #print(int_list)
            
            #Y!=0
            #if int_list[1] == 0:
            #    print(f"Error...\nEl valor de y={int_list[1]} debe ser diferente a 0\n")
            #X debe ser menor o igual a Y, y Y!=0
            if int_list[0] > int_list[1]:
                print(f"Error...\nEl valor de x={int_list[0]} es mayor al valor de y={int_list[1]}\n")
            #Colocar F en caso X/Y sea mayor a 99%.
            elif int_list[0] == int_list[1]:
                print("El tanque de gasolina está lleno: 'FUEL'")
            #Colocar E en caso X/Y sea menor a 1% del total.
            elif int_list[0] == 0:
                print("El tanque de gasolina está vacío: 'EMPTY'")
            else:
                #En otro caso, devolver el valor en porcentaje %
                print("El porcentaje de gasolina es:",round(int_list[0]/int_list[1],2)*100,"%")
                break
        except ValueError:
            print("Error, los valores ingresados no son números enteros")
        except ZeroDivisionError:
            print("El valor de Y es cero...\nIntenta de nuevo...")


if __name__ == "__main__":
    x=sol1()
    print(x)