man_a = open ('mbox.txt')       # de donde es el documentoo cuando sale esto man_a = open ('mbox-short.txt')
for linea in man_a:
    if linea.startswith('from:') :
        print(linea)
