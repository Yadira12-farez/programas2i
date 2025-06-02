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

def es_par(numero) :
    resultado = numero % 2 == 0 
    return resultado

num1 = float(input("ingrese un numero: "))
num2 = float(input("ingresa otro numero: ")) 
producto = num1 % num2
print("resultado es ", (producto))