import random

# Define las opciones del juego.
options = ('piedra', 'papel', 'tijera')

# Función para que el usuario elija una opción válida.
def choose_option():
    while True:
        user_option = input('Piedra, papel o tijera => ').lower()
        if user_option in options:
            return user_option
        else:
            print('Opción no válida. Inténtalo de nuevo.')

# Función para determinar el ganador de una ronda.
def determine_winner(user_option, computer_option):
    if user_option == computer_option:
        return 'Empate'
    elif (user_option == 'piedra' and computer_option == 'tijera') or \
         (user_option == 'papel' and computer_option == 'piedra') or \
         (user_option == 'tijera' and computer_option == 'papel'):
        return 'Usuario'
    else:
        return 'Computadora'

# Función principal del juego.
def run_game():
    computer_wins = 0
    user_wins = 0  
    rounds = 1

    while True:
        print('*' * 10)
        print(f'ROUND {rounds}')
        print('*' * 10)

        print('Puntuación actual:')
        print('Computadora:', computer_wins)
        print('Usuario:', user_wins)
        rounds += 1

        user_option = choose_option()
        computer_option = random.choice(options)

        print('Opción del Usuario =>', user_option)
        print('Opción de la Computadora =>', computer_option)

        winner = determine_winner(user_option, computer_option)
        if winner == 'Usuario':
            user_wins += 1
        elif winner == 'Computadora':
            computer_wins += 1

        print(winner, 'gana esta ronda.')

        if computer_wins == 2:
            print('El ganador es la Computadora')
            break

        if user_wins == 2:
            print('El ganador es el Usuario')
            break

run_game()
