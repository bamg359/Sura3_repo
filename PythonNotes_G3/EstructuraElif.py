
num1 = int(input("Num1"))
num2 = int(input("Num2"))

print("Seleccione 1. Sumar\n 2. Restar \n 3. Multiplicar \n 4. Dividir")


sel = int(input("Seleccione una opcion"))
if sel == 1:
    print("Suma")
    suma = num1 + num2
    print(f"El resultado de la suma es{suma}")
elif sel== 2:
    print("Resta")
else:
    print("Seleccione una opcion valida")        