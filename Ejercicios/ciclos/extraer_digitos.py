""" Realiza un programa en python:   
Que extraiga los digitos de la siguiente cadena de texto: text = '3hdk5haksj3kdmmzwqpeoco'
Que los ordene de menor a mayor y los devuelva en una cadena de Texto
Que sume todos los digitos y devuelva el reseultado de la suma total
Todos estos resultados deben ser mostrados por consola de manera simultanea """

text = '3hdk5haksj3kdmmz45eoco'

# Inicializa una lista para almacenar los dígitos extraídos
digitos = []

# Inicializa la suma total
suma_total = 0

# Itera a través de cada carácter en la cadena de texto
for caracter in text:
    # Verifica si el carácter es un dígito
    if caracter.isdigit():
        # Convierte el carácter a un entero y lo agrega a la lista de dígitos
        digitos.append(int(caracter))
        # Suma el dígito a la suma total
        suma_total += int(caracter)

# Ordena la lista de dígitos de menor a mayor
digitos_ordenados = sorted(digitos)

# Convierte la lista de dígitos ordenados en una cadena de texto
cadena_digitos_ordenados = ''.join(map(str, digitos_ordenados))

# Muestra los resultados por consola
print("Dígitos extraídos:", digitos)
print("Dígitos ordenados de menor a mayor:", cadena_digitos_ordenados)
print("Suma total de los dígitos:", suma_total)