#finalizar una iteracion con continue
while True : 
    line = input('ingresa un caracter : ')
    if line[0] == '#' : 
        continue
    if line == 'terminado' : 
        break
    print(line)
print('terminado')


for i in [5,4,3,2,1] : 
    print(i)
print('blastoff')

amigos = ['joseph', 'glenn', 'sally']
for amigos in amigos : 
    print('Feliz año nuevo : ', amigos)
print('terminado')