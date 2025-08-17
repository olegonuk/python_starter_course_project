"""Головний файл з функціями"""
import random
from art import text2art
from colorama import Fore
from prettytable import PrettyTable

def greeting_func(name):
    """ Вітання """
    return f'Вас вітає Розділ {name}"'


def greeting_game_func(welcome_text, style):
    """ Вітання """
    return Fore.WHITE + (text2art(welcome_text, font=style, chr_ignore=True))

#
# def finish_section_text():
#     """Функція друкування завершення секції"""
#     return "Дякую за участь! Гру завершено!"


def display_header_func(bot_header, style):
    """Функція друкування вітального хедера"""
    return Fore.WHITE + (text2art(bot_header, font=style, chr_ignore=True))


def get_random_item_func(lst):
    """Функція отримання випадкового елемента"""
    random_item = random.choice(lst)
    return random_item


def display_genre_func(lst, style):
    """Функція друкування списку жанрів"""
    return (text2art("List of available genres:\n", font=style, chr_ignore=True) +
            "\n".join(f'- {item}' for item in lst))


def get_genre_func(lst):
    """Функція отримання жанру елемента та друкування"""
    lst_genres = sorted(set(item['genre'] for item in lst))
    print(display_genre_func(lst_genres, 'fancy143'))

    while True:
        ask_genre = input("Оберіть жанр: ").strip()
        if ask_genre in lst_genres:
            return ask_genre

        print("Ви ввели невідомий жанр, будь ласка спробуйте ще раз!")
        continue


def filtered_lst_func(lst, genre):
    """Функція сортування списку елементів за жанром"""
    result = []
    for item in lst:
        if item['genre'].lower() == genre.lower():
            result.append(item)
    return result


def list_items_func(lst, name):
    """Функція друкування списку елементів"""
    print(text2art(f"List of {name}:\n", font="fancy143", chr_ignore=True))
    table = PrettyTable()
    table.align = "l"
    table.max_table_width = 120
    if "author" in lst[0]:
        table.field_names = ['№', 'Виконавець', 'Назва', 'Жанр']
        for num, elem in enumerate(lst, start=1):
            table.add_row([num, elem["author"], elem["title"], elem["genre"]])
    else:
        table.field_names = ['№', 'Назва', 'Жанр']
        for num, elem in enumerate(lst, start=1):
            table.add_row([num, elem["title"], elem["genre"]])
    return table


def display_elem_func(elem):
    """Функція друкування елементу"""
    table = PrettyTable()
    table.align = "l"
    table.max_table_width = 120
    if "author" in elem:
        table.field_names = ['Виконавець', 'Назва', 'Жанр', 'Чому']
        table.add_row([elem["author"], elem["title"], elem["genre"], elem["why"]])
    else:
        table.field_names = ['Назва', 'Жанр', 'Чому']
        table.add_row([elem["title"], elem["genre"], elem["why"]])
    return table


def open_info_func(lst):
    """Функція відкриває обраний елемент"""
    while True:
        try:
            item_number = int(input("Введіть номер зі списку, який хочете відкрити: "))
            if 0 < item_number <= len(lst):
                print(display_elem_func(lst[item_number - 1]))
                break
        except ValueError:
            print("Немає за таким номером!")


def finish_recom_section_text(name):
    """Функція друкування завершення секції Рекомендації"""
    return f"Розділ Рекомендації / \"{name}\" завершено!'"


def finish_section_text(name):
    """Функція друкування завершення секції"""
    return f"Розділ / \"{name}\" завершено!'"


def finish_game_text(name):
    """Функція друкування завершення секції ігр"""
    return f"Дякую за участь! Гру {name} завершено!"


def ask_continue_func(name, func=None):
    """Функція запитує, чи хоче користувач продовжити гру"""
    while True:
        continue_program = input(f"- Бажаєте продовжити Розділ {name}?\n"
                                 f"введіть Т(Так)/Н(Ні): ").strip().lower()
        if continue_program in {'т', 'y', 'так', 'yes'}:
            return True

        if continue_program in {"н", "n", "ні", "no"}:
            print(func)
            return False

        print("Невідома відповідь! Спробуйте ще раз!")


def exit_program_func():
    """Функція публікує повідомлення про завершення програми комбінацією символів «exit»"""
    return 'Шкода, що Ви вже покидаєте Нас, програму завершено!'
