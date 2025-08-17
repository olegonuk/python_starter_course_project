"""Розділ Гра Вгадай число"""
from random import randint
from utils.functions import greeting_game_func
from utils.functions import ask_continue_func
from utils.functions import finish_game_text
from data import list_greeting_game_text as welcome_text
from data import list_finish_game_text as lst_game_name

def number_error_func(value):
    """Функція публікує повідомлення про введення не числа"""
    return f'Ви ввели в поле "{value}" не число, будь ласка введіть числове значення!'


def bot_choice_number():
    """Функція обирає випадкове число для Чат-боту"""
    bot_number = randint(1, 20)
    return bot_number


def match_numbers_func(user_choice, attempt):
    """Функція публікує повідомлення про співпадіння чисел"""
    return f'Вітаю! Ви вгадали за {attempt} спроб(и). Ви ввели {user_choice}!'


def les_number_func(user_choice):
    """Функція публікує повідомлення що введене число менше"""
    return f'Нажаль введене Вами число {user_choice} менше!'


def more_number_func(user_choice):
    """Функція публікує повідомлення що введене число більше"""
    return f'Нажаль введене Вами число {user_choice} більше!'


def exit_program_func():
    """Функція публікує повідомлення про завершення програми «return»"""
    return 'Шкода, що Ви вже покидаєте Нас, гру завершено!'


def ask_user_number():
    """Функція зображає хід гри"""
    print(greeting_game_func(welcome_text[1], "fancy143"))  # Вітання

    bot_number = bot_choice_number()  # обирає випадкове число для Чат-бот
    tries = 0  # Змінна кількості спроб

    while True:
        user_number = input("Введіть варіант вашого числа або "
                            "\"return\" до попереднього меню: ").strip()

        if user_number == 'return':  # до попереднього меню
            print(exit_program_func())
            break
        try:
            user_number = int(user_number)
            tries += 1
        except ValueError:
            print(number_error_func(user_number))  # повідомлення про введення не числа
            continue

        if user_number == bot_number:
            print(match_numbers_func(user_number, tries))  # повідомлення про співпадіння чисел

            if not ask_continue_func(lst_game_name[1], finish_game_text(lst_game_name[1])):
                break

            bot_number = bot_choice_number()  # нове число для Чат-бот
            tries = 0  # скидання кількості спроб
            continue

        if user_number < bot_number:
            print(les_number_func(user_number))  # повідомлення що введене число менше
        else:
            print(more_number_func(user_number))  # повідомлення що введене число більше
