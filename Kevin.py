numero = int(input("Ingrese un numero: "))
def factorial (numero):
    if (numero == 0):
        return 1
    else:
        return numero* factorial(numero-1)
print(f"El factorial de {numero} es {factorial(numero)}  ")