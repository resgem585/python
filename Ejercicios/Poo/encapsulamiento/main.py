""" En este desafío, debes implementar la lógica de la clase "Usuario" que represente un usuario en una red social y utilizar encapsulamiento para proteger sus datos privados.

La clase debe tener las siguientes variables privadas:

name
age
friends (lista de diccionarios Usuario)
messages (lista de strings)
Además, debes proporcionar los siguientes métodos públicos:

addFriend(friend): agrega un usuario a la lista de amigos del usuario actual.
sendMessage(message, friend): agrega un mensaje a la lista de mensajes del usuario actual y al amigo especificado.
showMessages(): devuelve la lista de mensajes del usuario actual.
También debes tener definidos los getters y setters para acceder a los datos privados como el nombre y la edad, los cuales pueden ser modificados mediante su propio setter.

Ejemplo 1:

Input:

usuario1 = User("Juan", 20)
usuario2 = User("Maria", 25)
usuario1.addFriend(usuario2)
usuario1.sendMessage("Hola Maria!", usuario2)

usuario1.showMessages()

Output:

["Hola Maria!"]

Ejemplo 2:

Input:

usuario1 = User("Juan", 20)
usuario1.name = "Pepito"
print(usuario1.name)

Output:

"Pepito" """

class User:
    def __init__(self, name, age):
        # Inicializamos las propiedades privadas del usuario
        self._name = name
        self._age = age
        self._friends = []
        self._messages = []

    def add_friend(self, friend):
        # Método para agregar un amigo a la lista de amigos
        self._friends.append(friend)

    def send_message(self, message, friend):
        # Método para enviar un mensaje a un amigo
        self._messages.append(message)
        friend._messages.append(message)

    def show_messages(self):
        # Método para mostrar los mensajes del usuario
        return self._messages

    @property
    def name(self):
        # Getter para obtener el nombre del usuario
        return self._name

    @name.setter
    def name(self, value):
        # Setter para actualizar el nombre del usuario
        self._name = value

    @property
    def age(self):
        # Getter para obtener la edad del usuario
        return self._age

    @age.setter
    def age(self, value):
        # Setter para actualizar la edad del usuario
        self._age = value