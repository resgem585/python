def encontrar_palabras_repetidas(lista):
    palabras_repetidas = []
    palabras_procesadas = set()

    for palabra in lista:
        # Convierte la palabra a minúsculas para hacer la comparación insensible a mayúsculas y minúsculas
        palabra = palabra.lower()

        if palabra in palabras_procesadas:
            # Si la palabra ya ha sido procesada antes, la agregamos a la lista de palabras repetidas
            palabras_repetidas.append(palabra)
        else:
            # Si es la primera vez que vemos esta palabra, la registramos como procesada
            palabras_procesadas.add(palabra)

    return palabras_repetidas

# Ejemplo de uso:
mi_lista = ["Hola", "Hola", "Mundo", "Python", "mundo", "Python", "Python"]
repetidas = encontrar_palabras_repetidas(mi_lista)
print("Palabras repetidas:", repetidas)