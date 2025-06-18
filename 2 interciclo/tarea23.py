archivox = open('mbox.txt')
for queso in archivox : 
    print(queso)


man_a = open ('mbox.txt')
contador = 0 
for linea in man_a:
    contador = contador + 1
print('total de lineas', contador)