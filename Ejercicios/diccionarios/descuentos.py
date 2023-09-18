# Definimos un diccionario de descuentos para diferentes categorías de productos.
descuentos = {
    "productos lacteos": 0.1,
    "productos horneados": 0.3
}

# Mostramos los descuentos disponibles.
print("Descuentos disponibles:")
for categoria, descuento in descuentos.items():
    print(f"- {categoria} - {descuento*100}% de descuento.")

# Iniciamos un bucle infinito para procesar las compras.
while True:
    # Solicitamos al usuario que introduzca una categoría o 'cancelar' para salir.
    categoria = input("Introduce la categoría o 'cancelar' para salir: ")

    if categoria == "cancelar":
        # Si el usuario ingresa 'cancelar', salimos del bucle.
        print("Compra cerrada")
        break

    if categoria not in descuentos:
        # Si la categoría no tiene descuento, solicitamos el precio del producto.
        monto = float(input("Introduce el precio del producto: "))
        print(f"Monto a pagar: {monto}")
    else:
        # Si la categoría tiene un descuento válido, solicitamos el precio del producto.
        monto = float(input("Introduce el precio del producto: "))
        descuento = descuentos[categoria]
        monto_descuento = monto * (1 - descuento)
        # Calculamos el monto con descuento y lo mostramos.
        print(f"Descuento de {descuento*100}%. Por pagar: {monto_descuento}")

