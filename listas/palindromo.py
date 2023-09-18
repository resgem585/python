def es_palindromo(cadena):
    # Elimina los espacios en blanco y convierte la cadena a minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    # Comprueba si la cadena es igual a su inversa
    if cadena == cadena[::-1]:
        return True
    else:
        return False

# Solicita al usuario ingresar una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Llama a la función es_palindromo para verificar si es un palíndromo
if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
