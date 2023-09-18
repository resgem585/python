""" Este programa primero carga el JSON de ejemplo en un diccionario utilizando json.loads(json_str). Luego, itera a través de las claves del diccionario y agrega los elementos correspondientes a una lista llamada elementos. Puedes adaptar este programa para trabajar con archivos JSON o cambiar el contenido del JSON según tus necesidades.
 """

import json

# JSON de ejemplo como una cadena
json_str = '{"nombre": "Juan", "edad": 30, "ciudad": "Mexico"}'

# Carga el JSON en un diccionario
data = json.loads(json_str)

# Inicializa una lista para almacenar los elementos de las claves
elementos = []

# Itera a través de las claves y agrega los elementos a la lista
for clave, valor in data.items():
    elementos.append(valor)

# Imprime la lista de elementos
print(elementos)




