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

def raiz_babilonica(numero, tolerancia=1e-10, max_iter=1000):
    if numero < 0:
        raise ValueError 
    x = numero / 2.0
    for i in range(max_iter):
        x_nuevo = 0.5 * (x + numero / x)

        if abs(x - x_nuevo) < tolerancia:
            break
        x = x_nuevo
    return x

if __name__ == "__main__":
    try:
        numero = float(input("Ingresa un número positivo : "))
        resultado = raiz_babilonica(numero)
        print(f"La raíz cuadrada aproximada de {numero} es: {resultado}")
    
    except ValueError as e:
        print(f"Error: {e}")


#Contar dígitos de un número entero (ej: 456 → 3).

def contar_digitos(numero):
    return len(str(abs(numero))) 
num = int(input("Ingresa un número entero: "))
print(f"El número {num} tiene {contar_digitos(num)} dígitos.")

#Generar la secuencia de Fibonacci hasta un límite.

def fibonacci_hasta(limite):
    a, b = 0, 1
    while a <= limite:
        print(a, end=' ')
        a, b = b, a + b
limite = int(input("Ingresa el valor límite para la secuencia de Fibonacci: "))
print("Secuencia de Fibonacci:")
fibonacci_hasta(limite)

#Encontrar números primos en un rango dado.

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
inicio = int(input("Desde qué número quieres empezar: "))
fin = int(input("Hasta qué número quieres llegar: "))

print("Números primos en ese rango:")
for n in range(inicio, fin + 1):
    if es_primo(n):
        print(n)

#simular un temporizador(contar regresivamente desde N )

import time
def temporizador_regresivo(n):
    while n > 0:
        print(f"Tiempo restante: {n} segundos")
        time.sleep(1)
        n -= 1
    print("¡Tiempo terminado!")
N = int(input("Ingresa el número de segundos para el temporizador: "))
temporizador_regresivo(N)


#Leer archivos línea por línea hasta fin de archivo.

def leer_lineas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("Archivo no encontrado.")
archivo = input("Ingresa el nombre del archivo a leer (con extensión): ")
leer_lineas(archivo)

#mientras - while
#visualizar los 5 primero numero con mientras = while 

contador = 0
while contador <= 5:
    print("numero : ", contador)
    contador += 1