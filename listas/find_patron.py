def encontrar_patron(lista, patron):
    longitud_patron = len(patron)
    ocurrencias = []

    for i in range(len(lista) - longitud_patron + 1):
        if lista[i:i + longitud_patron] == patron:
            ocurrencias.append(i)

    return ocurrencias

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
mi_patron = [1]

resultados = encontrar_patron(mi_lista, mi_patron)
if resultados:
    print(f"El patrón {mi_patron} se encuentra en las posiciones: {resultados}")
else:
    print("El patrón no se encuentra en la lista.")
