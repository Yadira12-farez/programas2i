#Crea un mini programa que use al menos 3 funciones. Algunas ideas: •Agenda simple
#Agrega, muestra y busca contactos : •	Menú matemático interactivo (sumar, restar, multiplicar)
#El usuario elige operar (sumar, restar, multiplicar). : •	Juego de adivinanza con números
#El usuario intenta adivinar un número secreto del 1 al 10.
#1. calculadira basica 
def calculadora():
    print("Bienvenido a la calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        opcion = input("Elige una opción (1-5): ")
        if opcion == "5" :
            print("Gracias por utilizar esta calculadora.")
            break
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if opcion not in ["1", "2", "3", "4", "5"]:
            print("Opción no válida, intenta de nuevo.")
            continue
        elif opcion in ["1", "2", "3", "4"]:
            if opcion == "1" :
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
            elif opcion == "2" :
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
            elif opcion == "3" :
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            elif opcion == "4" :
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
                else:
                    print("Error: División por cero.")
        else:
            print("Opción no válida, intenta de nuevo.")

calculadora()

#2.promedio de notas 
def calcular_promedio():
    nota1 = float(input("Ingrese la Nota 1 de 0 a 10: "))
    nota2 = float(input("Ingrese la Nota 2 de 0 a 10: "))
    nota3 = float(input("Ingrese la Nota 3 de 0 a 10: "))

    promedio = (nota1 + nota2 + nota3) / 3
  

    if promedio < 5:
        estado = "Reprobado"
    elif promedio >= 5.1  and  promedio < 6.99:
        estado = "Regular"
    elif promedio >=7 and promedio < 8.99:
        estado = "Buena"
    else:
        estado = "Excelente"

    print(f"\n El Promedio del estudiante es:  {promedio}")
    print(f"\n El estudiante se encuentra en un estado: {estado}")
calcular_promedio()


#menu

def contactos(): 
    print("contactos son: ")
    print("1. Calculadora basica")
    print("2. Promedio de notas")
    opcion = input("eligue uno de los contactos (1/2) : ")

    x = float(input("ingresa un numero : "))
    y =float(input("ingresa otro numero : "))

    if opcion == "1" : 
        print(f"resultado es: ", (calculadora()))  
    elif opcion == "2" : 
        print(f"resultado es : ", (calcular_promedio()))

contactos()












