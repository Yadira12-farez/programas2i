##5 ejercicios que utilice archivos 
#3. Leer un archivo con números y calcular su promedio
numeros = []

with open("numeros.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea: 
            try:
                numeros.append(float(linea))
            except ValueError:
                print(f"No se pudo convertir la línea: {linea}")

if numeros:
    promedio = sum(numeros) / len(numeros)
    print(f"Promedio: {promedio}")
else:
    print("No hay números válidos en el archivo.")

