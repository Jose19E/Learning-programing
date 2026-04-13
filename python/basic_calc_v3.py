
# Pedir los números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar menú
print("####MENU####")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Promedio")
print("6. Todas las operaciones")

# Pedir opción
opcion = int(input("Elija una opción (1-6): "))

# Validar opción
if opcion < 1 or opcion > 6:
    print("Opción inválida")

else:
    if opcion == 1:
        print("Resultado:", num1 + num2)

    elif opcion == 2:
        print("Resultado:", num1 - num2)

    elif opcion == 3:
        print("Resultado:", num1 * num2)

    elif opcion == 4:
        if num2 == 0:
            print("Error: No se puede dividir entre 0")
        else:
            print("Resultado:", num1 / num2)

    elif opcion == 5:
        promedio = (num1 + num2) / 2
        print("Promedio:", promedio)

    elif opcion == 6:
        print("\n--- Resultados ---")
        print("Suma:", num1 + num2)
        print("Resta:", num1 - num2)
        print("Multiplicación:", num1 * num2)

        if num2 == 0:
            print("División: Error (división entre 0)")
        else:
            print("División:", num1 / num2)

        print("Promedio:", (num1 + num2) / 2)
