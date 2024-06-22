


init = int(input("Presione 1 para inicar la app"))

while init != 0:
    num1 = int(input("Num1"))
    num2 = int(input("Num2"))

    print("Seleccione\n 1. Sumar\n 2. Restar \n 3. Multiplicar \n 4. Dividir\n 5.Salir\n")


    sel = int(input("Seleccione una opcion"))
    if sel == 1:
        print("Suma")
        suma = num1 + num2
        print(f"El resultado de la suma es{suma}")
    elif sel== 2:
        print("Resta")
    elif sel== 5:
        init = 0    
    else:
        print("Seleccione una opcion valida")   