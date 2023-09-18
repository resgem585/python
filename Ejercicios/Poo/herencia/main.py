""" En este desafío, debes crear una jerarquía de clases mediante el uso de la herencia.

La clase base será Animal con las propiedades name, age y specie y un método getInfo que devuelve un objeto con la información del animal.

Luego, debes crear una clase Mammal que herede de Animal y tenga una propiedad adicional hasFur y un método getInfo que sobreescriba al del padre y incluya la información de hasFur.

Finalmente, debes crear una clase Dog que herede de Mammal y tenga una propiedad adicional breed y un método getInfo que sobreescriba al del padre y incluya la información de breed, al igual que el método bark que devuelva el string "woof!". Las propiedades de specie y hasFur deben estar incluídas como "dog" y True respectivamente desde la implementación por lo que no debe ser necesario pasar los valores a la hora de crear la instancia.

Ejemplo 1

Input:
bird = Animal("pepe", 1, "bird")
bird.getInfo()

Output:

{
  "name": "pepe",
  "age": 1,
  "specie": "bird",
}

Ejemplo 2

Input:
hippo = Mammal("bartolo", 3, "hippo", false)
hippo.getInfo()

Output:

{
  "name": "bartolo",
  "age": 3,
  "specie": "hippo",
  "hasFur": false,
}

Ejemplo 3

Input:
dog = Dog("fido", 4, "pastor aleman");
dog.bark()

Output:
"woof!" """

# Definición de la clase Animal
class Animal:
  # Constructor de la clase Animal
  def __init__(self, name, age, specie):
    self.name = name  # Nombre del animal
    self.age = age    # Edad del animal
    self.specie = specie  # Especie del animal

  # Método para obtener información del animal
  def getInfo(self):
    return {
      "name": self.name,
      "age": self.age,
      "specie": self.specie
    }

# Definición de la clase Mammal, que hereda de Animal
class Mammal(Animal):
  # Constructor de la clase Mammal
  def __init__(self, name, age, specie, hasFur):
    super().__init__(name, age, specie)  # Llama al constructor de la clase padre (Animal)
    self.hasFur = hasFur  # Indica si el mamífero tiene pelo

  # Método para obtener información del mamífero
  def getInfo(self):
    info = super().getInfo()  # Obtiene la información de la clase padre (Animal)
    info["hasFur"] = self.hasFur  # Agrega información específica de Mammal
    return info

# Definición de la clase Dog, que hereda de Mammal
class Dog(Mammal):
  # Constructor de la clase Dog
  def __init__(self, name, age, breed):
    super().__init__(name, age, "dog", True)  # Llama al constructor de la clase padre (Mammal)
    self.breed = breed  # Raza del perro

  # Método para obtener información del perro
  def getInfo(self):
    info = super().getInfo()  # Obtiene la información de la clase padre (Mammal)
    info["breed"] = self.breed  # Agrega información específica de Dog
    return info

  # Método específico de Dog para ladrar
  def bark(self):
    return "woof!"

# Crear una instancia de Animal llamada "response"
response = Animal("pepe", 1, "bird")

# Obtener información de la instancia "response"
info_response = response.getInfo()
print(info_response)  # Imprime la información del animal
