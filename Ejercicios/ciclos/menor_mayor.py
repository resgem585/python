def ordenar_lista(lista):
    n = len(lista)
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
                
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista

def SortNumbers(array):
  list=[]
  length=len(array)
  for i in range(length):
    minor=min(array)
    list.append(minor)
    array.remove(minor)

  return list

arrayNums = [2,4,1,1,3]

print(SortNumbers(arrayNums))
# Ejemplo de uso:
mi_lista = [64, 25, 12, 22, 11]
lista_ordenada = ordenar_lista(mi_lista)
print(lista_ordenada)

# Mayor a menor

def SortNumbersDescending(array):
    sorted_list = []
    
    while array:
        max_val = max(array)
        sorted_list.append(max_val)
        array.remove(max_val)
    
    return sorted_list

arrayNums = [2, 4, 1]

sorted_descending = SortNumbersDescending(arrayNums)
print(sorted_descending)

# Mayor a menor

def SortNumbersMax(array):
  list=[]
  length=len(array)
  for i in range(length):
    max1=max(array)
    list.append(max1)
    array.remove(max1)

  return list

arrayNums = [2,4,1,1,3,4,6,1]

print(SortNumbersMax(arrayNums))

# utilizando sorted

def SortNumbersAscending(array):
    sorted_list = sorted(array)
    return sorted_list

arrayNums = [2, 4, 1]

sorted_ascending = SortNumbersAscending(arrayNums)
print(sorted_ascending)

# utilizando sorted mayor a menor

def SortNumbersDescending(array):
    sorted_list = sorted(array, reverse=True)
    return sorted_list

arrayNums = [2, 4, 1]

sorted_descending = SortNumbersDescending(arrayNums)
print(sorted_descending)