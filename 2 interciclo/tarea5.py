def saludo (lang) : 
    if lang == 'es' :
        return('hola')
    elif lang =='fr' :
        return('bonjour')
    else :
        return('hello') 
        
print(saludo ('en'), 'glenn')
print(saludo ('fr'),'sally') 
print(saludo ('es'), 'michel')