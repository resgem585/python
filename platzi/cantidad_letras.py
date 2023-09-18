# Definición de la función count_letters_sensitive que toma una cadena de texto como entrada.
def count_letters_sensitive(phrase):
    # Se crea un diccionario vacío llamado characters para almacenar las cuentas de caracteres.
    characters = {}

    # Se inicia un bucle for que recorre cada carácter en la cadena phrase.
    for character in phrase:
        # Se verifica si el carácter actual ya está presente en el diccionario characters.
        if character in characters:
            # Si el carácter está en el diccionario, se incrementa su valor en 1 (ocurrencia adicional).
            characters[character] += 1
        else:
            # Si el carácter no está en el diccionario, se agrega con un valor inicial de 1.
            characters[character] = 1

    # Se devuelve el diccionario characters que contiene las cuentas de cada carácter.
    return characters

# Ejemplo de uso de la función count_letters_sensitive con una cadena de texto.
input_text = "Hola mundo"
result = count_letters_sensitive(input_text)

# Se imprime el resultado que muestra las cuentas de cada letra en la cadena,
# incluyendo mayúsculas y minúsculas por separado.
print(result)