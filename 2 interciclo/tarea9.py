# 1.Crear una función multiplicar(x, y) que retorne el producto de dos números. # esto es cuando defino 
def multiplicacion(x, y) : 
    return x * y 

resultado =  multiplicacion(6,7)
print("El resultado es:", resultado)


#ejemplo codigo escrito 

def multiplicar(x, y): 
    resultado = x * y 
    return resultado

numero1 = float(input("ingresa un numero : "))
numero2 = float(input("ingresa otro numero : "))
producto = numero1 * numero2 
print("multipñlicacion es : ", producto)

# 2.Crear una función es_par(numero) que retorne True si el número es par.
def es_par(numero) :
    return numero % 2 == 0 
print(es_par(4)) 
print(es_par(7)) 

#3.	Crear una función presentarse(nombre, edad) que imprima un mensaje con tus datos.
def presentarse(nombre, edad):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")
presentarse("Yadira", 20)

