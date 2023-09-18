def calculate_average(numbers):
  if len(numbers) == 0:
    raise ValueError("La lista está vacía")

  total = 0

  for num in numbers:
    if not isinstance(num, (int, float)):
      raise TypeError("La lista contiene elementos no numéricos")
    total += num

  return total / len(numbers)

response = calculate_average([3, 2, 3, 4, 5])
print(response)


# Segundo Ejemplo

def calculate_discounted_price(price, discount):
  # Verificar si price y discount son números (int o float)
  if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
    raise TypeError("El precio y el descuento deben ser números")

  # Verificar que price y discount sean valores positivos
  if price < 0 or discount < 0:
    raise ValueError("El precio y el descuento deben ser valores positivos")

  try:
    # Calcular el precio descontado
    discounted_price = price - (price * discount)
    return discounted_price

  except Exception as e:
    # Capturar errores inesperados y mostrar un mensaje de error personalizado
    raise Exception("Ha ocurrido un error inesperado: " + str(e))

# Llamar a la función calculate_discounted_price con un precio de 100 y un descuento del 20%
response = calculate_discounted_price(100, 0.2)
print(response)