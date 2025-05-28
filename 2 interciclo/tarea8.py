
# 1. Crear una función que imprima un mensaje
def saludo():
    print('¡Hola, mundo!')
saludo()

# 2. Función con un argumento
def saludar(nombre):
    print(f'Hola, {nombre}')
saludar("Yadira")

# 3. Suma de dos números
def sumar(a, b):
    return a + b
print(sumar(5, 7))

# 4. Calcular el salario
def computepay(horas, tarifa):
    if horas > 40:
        extra = horas - 40
        return 40 * tarifa + extra * tarifa * 1.5
    else:
        return horas * tarifa
print(computepay(45, 10))

# 5. Función para determinar el mayor carácter
def mayor_caracter(cadena):
    return max(cadena)
print(mayor_caracter("cuenca"))

# 6. Conversión de tipo
def convertir_a_flotante(valor):
    try:
        return float(valor)
    except ValueError:
        return None
print(convertir_a_flotante("3.1416"))

# 7. Función que retorna un saludo en diferentes idiomas
def saludo_idioma(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(saludo_idioma("fr"))

# 8. Comprobar si un número es par
def es_par(numero):
    return numero % 2 == 0
print(es_par(4))

# 9. Concatenar cadenas
def concatenar(cad1, cad2):
    return cad1 + cad2
print(concatenar("Hola ", "Yadira"))

# 10. Calcular promedio
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0
print(promedio([10, 8, 9]))

# 11. Contar vocales
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    return sum(1 for c in cadena if c in vocales)
print(contar_vocales("Universidad"))

# 12. Revertir cadena
def invertir(cadena):
    return cadena[::-1]
print(invertir("Cuenca"))

# 13. Tabla de multiplicar
def tabla(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
tabla(7)

# 14. Función sin parámetros
def mensaje():
    print("Primera línea de mensaje.")
    print("Segunda línea de mensaje.")
    print("Tercera línea de mensaje.")
mensaje()

# 15. Función que retorne el número más pequeño
def menor_valor(lista):
    return min(lista) if lista else None
print(menor_valor([3, 5, 1, 2]))

# 16. Calcular factorial
def factorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(factorial(5))

# 17. Determinar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
print(es_primo(11))

# 18. Repetir una cadena n veces
def repetir(cadena, n):
    return cadena * n
print(repetir("Hola ", 3))

# 19. Función con múltiples parámetros
def descripcion(nombre, edad, ciudad):
    print(f'{nombre} tiene {edad} años y vive en {ciudad}.')
descripcion("Yadira", 21, "Cuenca")

# 20. Verificar palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
print(es_palindromo("Anita lava la tina"))
