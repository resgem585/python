""" En la variable 'text' dispones de una cadena de texto. Debes contar las palabras y devolver cuantas veces se repiten cada una de ellas. Ejemplo : 'nadie' aparece 2 veces      
text = 'Creo que a veces es la gente que de la que nadie espera nada, la que hace cosas que nadie puede imaginar' """

text = 'Creo que a veces es la gente que de la que nadie espera nada, la que hace cosas que nadie puede imaginar'

# Dividir la cadena de texto en palabras
words = text.split()

# Inicializar un diccionario para contar las ocurrencias de cada palabra
word_counts = {}

# Contar las ocurrencias de cada palabra
for word in words:
    # Eliminar signos de puntuación y convertir a minúsculas para evitar contar palabras con diferente capitalización como distintas
    word = word.strip('.,¡!¿?').lower()
    
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Imprimir el resultado
for word, count in word_counts.items():
    print(f"'{word}' aparece {count} veces")
