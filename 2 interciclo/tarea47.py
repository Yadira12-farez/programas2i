# Ejercicios con Listas y Diccionarios en Python

# Ejercicio 1
lista = ["manzana", "banana", "pera", "uva", "naranja"]
for i, elemento in enumerate(lista):
    print(f"Índice {i}: {elemento}")

# Ejercicio 11
palabras = input("Ingresa varias palabras separadas por espacio: ").split()
mas_larga = max(palabras, key=len)
print("Palabra más larga:", mas_larga)

# Ejercicio 21
texto = input("Escribe una línea de texto: ").lower().split()
frecuencia = {}
for palabra in texto:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print(frecuencia)

# Ejercicio 31
try:
    with open("datos.txt", "r") as archivo:
        palabras = archivo.read().lower().split()
        conteo = {}
        for palabra in palabras:
            conteo[palabra] = conteo.get(palabra, 0) + 1
        top3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
        print("Top 3 palabras más repetidas:", top3)
except FileNotFoundError:
    print("Archivo no encontrado.")


# Ejercicio 41
productos = {"leche": 1.20, "pan": 0.50, "huevos": 1.80, "queso": 2.00, "arroz": 1.00}
consulta = input("Producto a buscar: ").lower()
print(f"Precio de {consulta}: ${productos.get(consulta, 'No disponible')}")