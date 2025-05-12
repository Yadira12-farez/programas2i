#Sumar números ingresados por el usuario hasta que ingrese 0.
numero1 = int(input("ingresa un numero"))
numero2 = int(input("ingrese el numero"))
print("resultado de la suma es: ", numero1 + numero2)

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
x = int(input("ingresa un numero"))
if x > 5: 
     print("x es mayor que 5")
else :
     print("x no es mayor que 5")

#Validar contraseña (repetir hasta que coincida con una guardada).
contraseña = "yadira"

while True:
    entrada = input("Ingresa la contraseña: ")
    
    if entrada == contraseña :
        print("Contraseña correcta. ")
        break
    else:
        print("Contraseña incorrecta.")
#Simular un cajero automático (menú: retirar, depositar, salir).

saldo = 100

def mostrar_menu(): 
    print("\n--- Cajero Automático ---")
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cantidad = float(input("¿Cuánto deseas retirar? "))
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: ${saldo:.2f}")
        else:
            print("Fondos insuficientes.")
    
    elif opcion == "2":
        cantidad = float(input("¿Cuánto deseas depositar? "))
        saldo += cantidad
        print(f"Depósito exitoso. Saldo actual: ${saldo:.2f}")
    
    elif opcion == "3":
        print(f"Tu saldo actual es: ${saldo:.2f}")

    elif opcion == "4":
        print("Gracias por usar el cajero. Hasta pronto.")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")

#Calcular la raíz cuadrada por aproximación (método babilónico).

#Contar dígitos de un número entero (ej: 456 → 3).

#Generar la secuencia de Fibonacci hasta un límite.

#Encontrar números primos en un rango dado.

#Simular un temporizador (contar regresivamente desde N).

#Leer archivos línea por línea hasta fin de archivo.

#mientras - while
#visualizar los 5 primero numero con mientras = while 

contador = 0
while contador <= 5:
    print("numero : ", contador)
    contador += 1