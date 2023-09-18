# Importamos la clase Product del módulo 'product'
from product import Product

# Definimos la clase Article que hereda de Product
class Article(Product):
  def addToCart(self):
    return f"Agregando {self.quantity} unidades del artículo {self.name}"

# Definimos la clase Service que hereda de Product
class Service(Product):
  def addToCart(self):
    return f"Agregando el servicio {self.name} al carrito"

# Definimos la clase Cart que representa un carrito de compras
class Cart:
  def __init__(self):
    # Inicializamos la lista de productos vacía
    self.products = []

  def addProduct(self, product):
    # Llama al método addToCart del producto y agrega el producto a la lista
    product.addToCart()
    self.products.append(product)

  def deleteProduct(self, product):
    # Elimina el producto de la lista de productos en función de su nombre
    self.products = [item for item in self.products if item.name != product.name]

  def calculateTotal(self):
    # Calcula el precio total de los productos en el carrito
    total = sum(item.price * item.quantity for item in self.products)
    return total

  def getProducts(self):
    # Devuelve la lista de productos en el carrito
    return self.products

# Creamos instancias de Article y Service
book = Article("Libro", 100, 2)
course = Service("Curso", 120, 1)

# Creamos un carrito y agregamos los productos
cart = Cart()
cart.addProduct(book)
cart.addProduct(course)

# Calculamos el total de la compra y lo imprimimos
total = cart.calculateTotal()
print(total)
