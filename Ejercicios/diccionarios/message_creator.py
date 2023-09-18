def message_creator(text):
    # Definimos un diccionario de respuestas.
    respuestas = {
        'computadora': "Con mi computadora puedo programar usando Python",
        'celular': "En mi celular puedo aprender usando la app de Platzi",
        'cable': "¡Hay un cable en mi bota!"
    }

    # Comprobamos si 'text' está en las claves del diccionario 'respuestas'.
    if text in respuestas.keys():
        # Si está, retornamos la respuesta correspondiente.
        return respuestas[text]
    else:
        # Si no está, retornamos 'Artículo no encontrado'.
        return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)

def message_creator(text):
    # Usamos una estructura de selección múltiple (if-elif-else) para determinar la respuesta.
    if text == 'computadora':
        return 'Con mi computadora puedo programar usando Python'
    elif text == 'celular':
        return 'En mi celular puedo aprender usando la app de Platzi'
    elif text == 'cable':
        return '¡Hay un cable en mi bota!'
    else:
        # Si no se encuentra 'text' en las opciones, retornamos 'Artículo no encontrado'.
        return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)
