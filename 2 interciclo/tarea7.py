#reescriba el calculo de su salario con una hora y media para las horas extras y cree una funcion llamada computepay ( calcular salario) que toma dos parametros ( horas  y tarifa.)
#ingresar horas : 45
#ingresar tarifa : 10

def computepay(horas, tarifa):
    if horas > 40:
        horas = 40
        horas_extra = horas - 40
        pago = (horas * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        pago = horas * tarifa
    return pago

horas = float(input("Ingresar horas: "))
tarifa = float(input("Ingresar tarifa: "))
salario = computepay(horas, tarifa)
print("Salario:", salario)
