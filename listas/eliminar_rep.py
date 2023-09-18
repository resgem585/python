#Crea una funcion que regrese una lista sin repeticiones

def eliminar_repeticiones(lista):
    # Convierte la lista en un conjunto para eliminar duplicados
    conjunto_sin_repeticiones = set(lista)
    
    # Convierte el conjunto de nuevo en una lista
    lista_sin_repeticiones = list(conjunto_sin_repeticiones)
    
    return lista_sin_repeticiones

# Ejemplo de uso:
mi_list = ['hola', 'hola', 2, 3, 4, 4, 5]
resultado = eliminar_repeticiones(mi_list)
print(resultado)





