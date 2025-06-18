#1Conteo Regresivo con while
numero = 10

while numero >= 1:
    print(numero)
    numero -= 1

print("¡Despegue!")

#2Adivina la Palabra Secreta (while y break)
palabra_secreta = "luna"

while True:
    intento = input("Ingresa la palabra secreta: ")
    
    if intento == palabra_secreta:
        print("¡Has adivinado la palabra!")
        break
    else:
        print("Inténtalo de nuevo.")

#3Procesador de Entradas con continue

while True:
    texto = input("Ingresa un texto: ")

    if texto == "#":
        continue
    elif texto == "listo":
        print("¡Procesamiento terminado!")
        break
    else:
        print(texto.upper())

#4Lista de Invitados con for
invitados = ['Ana', 'Luis', 'Carla', 'Pedro']

for nombre in invitados:
    print(f"Hola {nombre}, ¡bienvenida a la fiesta!")

#5Encontrando el Número Mayor (for)
numeros = [3, 41, 12, 9, 74, 15, 1, 55]
mayor_hasta_ahora = -1

for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero

print("El número más grande es:", mayor_hasta_ahora)

#6Conteo de Elementos Pares (for y condicional)
numeros = [2, 5, 8, 11, 14, 17, 20, 23]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print("Cantidad de números pares:", contador)

#7
numeros = [10, 20, 30, 40, 50]
suma_total = 0

for numero in numeros:
    suma_total += numero

print("La suma total es:", suma_total)

#8Cálculo del Promedio (for)
numeros = [10, 15, 20, 25, 30]
promedio = 0
contador = 0

for numeros in numeros : 
    suma_total += numero
    contador += 1

promedio = suma_total / contador
print("Promedio es:", promedio)

#9Filtrando Números Mayores que un Valor (for)
numeros = [5, 25, 12, 33, 18, 45, 7]
umbral = int(input("Ingresa un numero: "))

for numero in numeros:
    if numero > umbral:
        print(numero)

#10Búsqueda de un Valor Específico (for y booleano)
numeros = [9, 41, 12, 3, 74, 15]
encontrado = False

for numero in numeros:
    if numero == 3:
        encontrado = True
        break

print("El valor 3 fue encontrado:", encontrado)
 
 #11Encontrando el Número Menor (for y None)
numeros = [30, 10, 5, 25, 50, 2]
menor_hasta_ahora = None

for numero in numeros:
    if menor_hasta_ahora is None:
        menor_hasta_ahora = numero
    elif numero < menor_hasta_ahora:
        menor_hasta_ahora = numero

print("El número más pequeño es:", menor_hasta_ahora)

#12¿Infinito o No? (Conceptual)
#bucle infinito 
n = 5
while n < 0 :
    n = n - 1
    print('enjaborar')
    print('enjuagar')
print('secar') 

n = 0
while n < 10:
    print("Iterando...")
    n += 1
print("Bucle terminado")


