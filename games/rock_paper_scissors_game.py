"""Розділ Гра Камінь-Ножиці-Папір"""
import random
from utils.functions import greeting_game_func
from utils.functions import ask_continue_func
from utils.functions import finish_game_text
from data import list_greeting_game_text as welcome_text
from data import list_finish_game_text as lst_game_name

lst_move = ['камінь', 'ножиці', 'папір']  # список ходів
# Виграшні комбінації для користувача
user_win_combinations = {
    ("камінь","ножиці"),
    ("ножиці","папір"),
    ("папір","камінь"),
}
lst_users = ['Користувач', 'Чат-бот']  # список учасників
collection = {}  # збереження ходу

def wrong_choice_func(value):
    """Функція публікує повідомлення про не коректний ввід"""
    return (f'Ви ввели в поле "{value}", що не є коректним ходом. '
            f'Введіть: Камінь, Ножиці або Папір!"')


def bot_choice_move():
    """Функція обирає рандомно хід для Чат-боту"""
    bot_choice = random.choice(lst_move)
    return bot_choice


def info_choice_func(user, move):
    """Функція публікує повідомлення про обраний хід"""
    return f'{user} обрав: "{move}"'


def draw_moves_func(user_choice, bot_choice):
    """Функція публікує повідомлення про нічию"""
    return f'Оу, Нічия! Ваш хід "{user_choice}" Чат-бот також "{bot_choice}"!'


def wining_message_func(user_choice, bot_choice):
    """Функція публікує повідомлення про виграш користувача"""
    return f'Вітаємо! Ви перемогли з комбінацією "{user_choice}" перемагає "{bot_choice}"!'


def losing_message_func(user_choice, bot_choice):
    """Функція публікує повідомлення про програш користувача"""
    return f'Нажаль Ви програли з комбінацією "{user_choice}" проти "{bot_choice}"!'


def exit_program_func():
    """Функція публікує повідомлення про завершення програми «return»"""
    return 'Шкода, що Ви вже покидаєте Нас, гру завершено!'


def ask_user_move():
    """Функція зображає хід гри"""
    print(greeting_game_func(welcome_text[0], "fancy143"))  # Вітання

    while True:
        user_move = input('Введіть варіант вашого ходу: '
                          '"Камінь, Ножиці, Папір" або '
                          '\"return\" до попереднього меню: ').strip().lower()

        if user_move == "return":  # до попереднього меню
            print(exit_program_func())
            break

        if user_move not in lst_move:
            print(wrong_choice_func(user_move))  # повідомлення про не коректний ввід
            continue

        bot_move = bot_choice_move()  # обирає рандомно хід

        collection[lst_users[0]] = user_move  # збереження ходу
        collection[lst_users[1]] = bot_move  # збереження ходу

        # Виводимо всі ходи гравців
        for user, move in collection.items():
            print(info_choice_func(user, move))  # повідомлення про обраний хід

        if user_move == bot_move:
            print(draw_moves_func(user_move, bot_move))  # повідомлення про нічию
        elif (user_move, bot_move) in user_win_combinations:
            print(wining_message_func(user_move, bot_move))  # повідомлення про виграш користувача
        else:
            print(losing_message_func(user_move, bot_move))  # повідомлення про програш користувача

        if not ask_continue_func(lst_game_name[0], finish_game_text(lst_game_name[0])):
            break
