#tarea en grupo 4: 
# •	Conversor de temperatura (Celsius a Fahrenheit y viceversa)
def convertir(valor, temp): 
    if temp == "C": 
        return(valor * 9/5) + 32 
    elif temp == "F":
        return(valor - 32) * 5/9
valor = float(input("ingresar la temperatura : "))
temp = input("ingresa: C para celsius, f para fahrenheit es : ").upper()
print(f"convertir es: ", (valor , temp)) 

