<<<<<<< HEAD
#Pedir numeros
num1 = float(input("Ingrese el primer numero:"))
num2 = float(input("ingrese el segundo numero:"))

#Mostrar Menu

print("####MENU####")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Promedio")
print("6. Todas las operaciones")

opcion = int(input("Seleccione una opcion (1-6):"))

    #validar opcion
if opcion <1 or opcion >6:
    print("Opcion Invalida")

else:
    if opcion == 1:
        print("Resultado:", num1 +num2)
    
    elif opcion == 2:
        print("Resultado:", num1 - num2)
    
    elif opcion == 3:
        print("Resultado", num1 * num2)
    
=======

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

>>>>>>> 03ef4d6d2e8a687a693d422358df72a8343c36a9
    elif opcion == 4:
        if num2 == 0:
            print("Error: No se puede dividir entre 0")
        else:
<<<<<<< HEAD
            print("Resultado", num1 / num2)

    elif opcion == 5:
        promedio=(num1+num2)/2
        print("Promedio:",promedio)

    elif opcion == 6:
        print("####Resultados####")
        print("Suma:", num1 + num2)
        print("Resta:", num1 - num2)
        print("Multiplicacion:", num1 * num2)
       
        if num2 == 0:
            print("Division: Error (No se puede dividir entre 0)")
        else:
            print("Division:", num1 / num2)
        
        print("Resultado:", (num1 + num2) / 2)

        
        





        

     
=======
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
>>>>>>> 03ef4d6d2e8a687a693d422358df72a8343c36a9
