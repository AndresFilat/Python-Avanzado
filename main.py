import os
import random

INDEX_IMG_WIN = 11
INDEX_IMG_LOSE = 10

# color
colors = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "purple": 35,
    "cian": 36
}


# start
def start_color(color):
    return f'\033[;{colors[color]}m'


# end
END_COLOR = '\033[0;m'


def print_logo(finish=False):
    if finish:
        print(f'''{start_color("blue")}
                    ╔═════════════════════════════════════════════╗
                    ║                                             ║
                    ║        █████   █████   █   █   █████        ║
                    ║        █       █   █   ██ ██   █            ║
                    ║        █████   █████   █ █ █   █████        ║
                    ║        █   █   █   █   █   █   █            ║
                    ║        █████   █   █   █   █   █████        ║
                    ║                                             ║
                    ║        █████   █   █   █████   █████        ║
                    ║        █   █   █   █   █       █   █        ║
                    ║        █   █   █   █   █████   █  █         ║
                    ║        █   █    █ █    █       █   █        ║
                    ║        █████     █     █████   █   █        ║
                    ║                                             ║
                    ╚═════════════════════════════════════════════╝
        {END_COLOR}''')
    else:
        print(f'''{start_color("cian")}
                    ╔═══════════════════════════════════════════════════════════╗
                    ║                                                           ║
                    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
                    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
                    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
                    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
                    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
                    ║                                                           ║
                    ║                    Elige una dificultad                   ║
                    ║                         1. Facil                          ║
                    ║                         2. Medio                          ║
                    ║                         3. Dificil                        ║
                    ╚═══════════════════════════════════════════════════════════╝
        {END_COLOR}''')


def search_images():
    strike0 = ''''''
    strike1 = f'''{start_color("yellow")}







        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike2 = f'''{start_color("yellow")}
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike3 = f'''{start_color("yellow")}
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike4 = f'''{start_color("yellow")}
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   {start_color("red")}d   b
        {start_color("yellow")}__║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike5 = f'''{start_color("yellow")}
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    {start_color("red")}/ \\
          ║   d   b
        {start_color("yellow")}__║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike6 = f'''{start_color("yellow")}
          ╔═════╦  
          ║
          ║
          ║
          ║     {start_color("red")}│
          ║    / \\
          ║   d   b
        {start_color("yellow")}__║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike7 = f'''{start_color("yellow")}
          ╔═════╦  
          ║
          ║
          ║    {start_color("red")}─┼─
          ║     │
          ║    / \\
          ║   d   b
        {start_color("yellow")}__║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike8 = f'''{start_color("yellow")}
          ╔═════╦  
          ║
          ║
          ║   {start_color("red")}┌─┼─┐
          ║     │
          ║    / \\
          ║   d   b
        {start_color("yellow")}__║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    strike9 = f'''{start_color("yellow")}
          ╔═════╦  
          ║
          ║     {start_color("red")}@
          ║   ┌─┼─┐
          ║     │
          ║    / \\
          ║   d   b
        {start_color("yellow")}__║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    losser = f'''{start_color("red")}
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / \\
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

{END_COLOR}'''
    winner = f'''{start_color("blue")}
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡TU GANAS!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / \\
    |_____________|/       d   b

{END_COLOR}'''
    return {0: strike0, 1: strike1, 2: strike2, 3: strike3, 4: strike4, 5: strike5, 6: strike6, 7: strike7, 8: strike8,
            9: strike9, 10: losser,
            11: winner}


def choose_word():
    with open('./archivos/data.txt', 'r', encoding='utf-8') as dictionary:
        content = dictionary.read()
        content = content.upper()
        split_words = content.split('\n')
        words = []
        flag = True
        while flag:
            try:
                difficulty = int(input(f'{start_color("cian")}>> '))
                if difficulty > 0 and difficulty <= 3:
                    if difficulty == 1:
                        for word in split_words:
                            if len(word) <= 5:
                                words.append(word)
                    elif difficulty == 2:
                        for word in split_words:
                            if len(word) > 5 and len(word) <= 10:
                                words.append(word)
                    elif difficulty == 3:
                        for word in split_words:
                            if len(word) > 10:
                                words.append(word)
                    flag = False
                else:
                    print(f"{start_color('red')}Eeh, no tenemos ese nivel ^^'")
                    continue
            except ValueError:
                print(f'{start_color("red")}Eh no ._.')
                continue
        word = random.choice(words)
    replace_characters = {
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U",
    }
    for a, b in replace_characters.items():
        word = word.replace(a, b)
    return word


def new_word_props():
    word = choose_word()
    index_letter = {i[0]: i[1] for i in enumerate(word)}
    discovered = [f'{start_color("red")}- {END_COLOR}' for _ in range(len(index_letter))]
    strikes = 0
    letters_available = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O',
                         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                         'X', 'Y', 'Z']
    return word, index_letter, discovered, strikes, letters_available


def compare_letters(selected_letter, word, discovered):
    fail = True
    for index, letter in enumerate(word):
        if letter == selected_letter:
            discovered[index] = selected_letter + ''
            fail = False
    return discovered, fail


def current_game(images, strikes, letters, invalid_letter=False):
    os.system('cls')
    print(
        f'{start_color("cian")}Recuerda que solo puedes usar estas letras -> {END_COLOR}'
        f'{start_color("green")}{"  ".join(letters)}{END_COLOR}')
    print(images.get(strikes))
    if invalid_letter:
        print(f"{start_color('red')}Que gracioso -.-")


def return_word(discovered, removing_spaces=True):
    word = ''.join(discovered)
    return word.replace(' ', '') if removing_spaces else word


def positive_answer():
    while True:
        again = input(
            f'''
{start_color("cian")}¿Otra partida ^^? (s/n)
>> ''')
        if again.lower() in ('s', 'n'):
            print_logo()
            return again.lower() == 's'
        else:
            print(f'\n{start_color("red")}._. que ingresaste? Prueba de nuevo')


def lose(strikes, images, letters_available, word):
    if strikes == INDEX_IMG_LOSE:
        current_game(images, INDEX_IMG_LOSE, letters_available)
        print(
            f"{start_color('cian')}"
            f"Perdiste! Te concedo una revancha, juega de nuevo! Ah por cierto la palabra era '{word}'")
        return True
    else:
        return False


def win(strikes, images, letters_available, word, discovered):
    if return_word(discovered) == word:
        current_game(images, INDEX_IMG_WIN, letters_available)
        print(
            f"{start_color('blue')}Asi se hace! {start_color('cian')}Fallaste {strikes} veces,"
            f"{start_color('blue')}en efecto la palabra era '{return_word(discovered)}'{END_COLOR}")
        return True
    else:
        return False


def exe():
    print_logo()
    images = search_images()
    letter_available = False
    word, letter_index, discovered, strikes, letters_available = new_word_props()
    while True:
        current_game(images, strikes, letters_available, invalid_letter=letter_available)
        letter_available = False
        letter = input(
            f'{start_color("purple")}¡Ingresa una letra!, me pregunto cual sera la correcta...{END_COLOR}\n'
            f'{return_word(discovered, removing_spaces=False)}\n'
            f'{start_color("cian")}>> ').upper()
        try:
            index = letters_available.index(letter)
            letters_available[index] = ''
        except ValueError:
            letter_available = True
            continue
        discovered, fail = compare_letters(letter, word, discovered)
        if fail:
            strikes += 1
        loser = lose(strikes, images, letters_available, word)
        winner = win(strikes, images, letters_available, word, discovered)
        if loser or winner:
            if positive_answer():
                word, letter_index, discovered, strikes, letters_available = new_word_props()
                continue
            else:
                print_logo(finish=True)
                print(f'{start_color("cian")}Bueno almenos nos divertimos :)\n'
                      f'Gracias por jugar ^^')
                break


if __name__ == '__main__':
    os.system('cls')
    exe()
