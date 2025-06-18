#5 ejercicios que utilice archivos 
#2. Guardar los nombres y edades de varias personas
with open("personas.txt", "w") as archivo:             # 'w' es la escritura 
    for _ in range(3):  # Puedes cambiar el número
        nombre = input("Ingrese el nombre: ")
        edad = input("Ingrese la edad: ")
        archivo.write(f"{nombre} - {edad}\n")
