# Definición de la función find_set_intersection que calcula la intersección de una lista de conjuntos.
def find_set_intersection(sets):
    # Verificar si la lista de conjuntos está vacía.
    if len(sets) == 0:
        # Si está vacía, devolver un conjunto vacío.
        return set()
    
    # Inicializar la variable 'intersection' con el primer conjunto en la lista.
    intersection = sets[0]
    
    # Iterar a través de los conjuntos restantes en la lista.
    for item in sets[1:]:
        # Calcular la intersección acumulativa con cada conjunto en la lista.
        intersection = intersection.intersection(item)
    
    # Devolver el conjunto resultante, que es la intersección de todos los conjuntos en la lista.
    return intersection

# Llamar a la función find_set_intersection con una lista de tres conjuntos.
response = find_set_intersection([
    {1, 2, 3, 4},
    {2, 3, 4, 5},
    {3, 4, 5, 6}
])

# Imprimir la respuesta, que es la intersección de los conjuntos.
print(response)