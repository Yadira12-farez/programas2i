#5 ejercicios que utilice archivos 
#1Leer un archivo de texto y contar cuántas líneas tiene
with open("mbox1.txt", "r") as archivo :
  lineas = archivo.readlines()
print(f"Cantidad de líneas: {len(lineas)}")

