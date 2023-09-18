#Multiplica dos numeros sin usar el operador de multiplicacion

def multiplicar(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

# Ejemplo de uso:
resultado = multiplicar(5, 3)
print(resultado)  # Esto imprimirá 15