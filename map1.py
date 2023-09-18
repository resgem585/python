#Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.
#La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada.

#Ejemplo 1:

#Input: [2, 4, 5, 6, 8]
#Output: [4, 8, 10, 12, 16]

#Ejemplo 2:

#Input: [1, 1, -2, -3]
#Output: [2, 2, -4, -6]

def multiply_numbers(numbers):
    # Utiliza map para aplicar la función lambda a cada elemento de la lista
    result = list(map(lambda x: x * 2, numbers))
    return result

# Ejemplo 1
input_list1 = [2, 4, 5, 6, 8]
output_list1 = multiply_numbers(input_list1)
print(output_list1)  # Output: [4, 8, 10, 12, 16]

# Ejemplo 2
input_list2 = [1, 1, -2, -3]
output_list2 = multiply_numbers(input_list2)
print(output_list2)  # Output: [2, 2, -4, -6]





