""" En este desafío, deberás crear la lógica para un automóvil mediante el uso de clases.

Deberás implementar la lógica necesaria en la clase Car de tal manera que nos pueda servir de base para crear nuevos autos que reciba los siguientes parametros:

brand: Marca del auto
model: Modelo del auto
year: Año del auto
mileage: kilometraje del auto
state: El estado por defecto del auto será false, indicando que el - auto se encuentra apagado.
Además, deberás implementar los siguientes métodos para hacer funcional los vehículos creados con la clase Car

turnOn(): Método que encenderá el auto.
turnOff(): Método que apagará el auto.
drive(kilometers): Con este método podremos aumentar el kilometraje según los kilómetros dados pero solo si el auto está encendido. En caso contrario, deberá mostrar el siguiente mensaje de error: "El auto está apagado".
Recuerda manejar los errores como una Exception

Ejemplo 1:

Input:
toyota = Car("Toyota", "Corolla", 2020, 0);
toyota.turnOn();
toyota.drive(100);
toyota.mileage


Output: 100 """

# Definición de la clase Car (Coche)

class Car:
    # Constructor de la clase, inicializa las propiedades del coche.
    def __init__(self, brand, model, year, mileage):
        self.brand = brand  # Marca del coche
        self.model = model  # Modelo del coche
        self.year = year    # Año del coche
        self.mileage = mileage  # Kilometraje del coche
        self.state = False  # Estado del coche (apagado por defecto)

    # Método para encender el coche
    def turnOn(self):
        if not self.state:  # Si el coche no está encendido
            self.state = True  # Enciende el coche
        else:
            print("El auto ya esta encendido.")  # Muestra un mensaje si ya está encendido

    # Método para apagar el coche
    def turnOff(self):
        if self.state:  # Si el coche está encendido
            self.state = False  # Apaga el coche
        else:
            print("El auto ya está apagado.")  # Muestra un mensaje si ya está apagado

    # Método para conducir el coche y aumentar el kilometraje
    def drive(self, kilometers):
        if self.state:  # Si el coche está encendido
            if kilometers >= 0:  # Asegura que la cantidad de kilómetros sea positiva
                self.mileage += kilometers  # Aumenta el kilometraje
            else:
                print("Error: La cantidad de kilómetros debe ser un valor positivo.")
        else:
            raise Exception("El auto esta apagado.")  # Lanza una excepción si el coche está apagado

# Ejemplo 1: Encender el coche, conducir 100 kilómetros y verificar el kilometraje
toyota = Car("Toyota", "Corolla", 2020, 0)
toyota.turnOn()
toyota.drive(100)
print(toyota.mileage)  # Output: 100

# Ejemplo 2: Apagar el coche y tratar de conducir 100 kilómetros (debería generar una excepción)
toyota.turnOff()
try:
    toyota.drive(100)
except Exception as e:
    print(f"Exception: {e}")  # Output: Exception: El auto está apagado
