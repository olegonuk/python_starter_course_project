"""Розділ Анекдот"""
import random
import pyjokes
from deep_translator import GoogleTranslator
from tqdm import tqdm
from prettytable.colortable import ColorTable, Themes
from utils.functions import display_header_func
from utils.functions import get_genre_func
from utils.functions import ask_continue_func
from utils.functions import finish_section_text

from data import list_jokes_genres as lst_joke_genres
from data import list_recommendations_en as lst_names_en
from data import list_recommendations_uk as lst_names_uk


lst_jokes_uk = []

def get_joke_func(category="all"):
    """Функція отримання Анекдота"""
    jokes_list = pyjokes.get_jokes(category=category)
    return random.choice(jokes_list)


def get_random_item_func(lst):
    """Функція отримання випадкового елемента"""
    random_item = random.choice(lst)
    return random_item['genre']


def display_joke_func(lst):
    """Функція друкування Анекдота"""
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.align = "l"
    table.field_names = ['№', 'Жанр', 'Анекдот']
    table.max_table_width = 120
    for num, elem in enumerate(lst, start=1):
        for genre, joke_text in elem.items():
            table.add_row([num, genre, joke_text])
    return table


def ask_for_joke():
    """Функція зображення розділу Анекдот"""
    if not pyjokes:
        print("Pyjokes is not installed!")
        return

    while True:
        print(display_header_func(f'Section|{lst_names_en[3]}', 'fancy142'))

        user_subsection_choice = input(f"Розділ \"{lst_names_uk[3]}\":\n"
                                       "- За жанром №1\n"
                                       "- Список анекдотів №2\n"
                                       "- Випадковий анекдот №3\n"
                                       "Введіть 'return' до попереднього меню\n: ").strip().lower()
        if user_subsection_choice == 'return':  # до попереднього меню
            break

        if user_subsection_choice not in ['1', '2', '3']:
            print('Ви ввели недійсне число. Будь ласка, введіть число від 1 до 3 або "return"')
            continue

        match user_subsection_choice:
            case '1':
                genre = get_genre_func(lst_joke_genres)
                bot_joke_en = get_joke_func(genre)  # отримання Анекдота
                for _  in tqdm(range(2), desc="Переклад анекдоту"):
                    bot_joke_uk = GoogleTranslator(source='en', target='uk').translate(bot_joke_en)
                print(display_joke_func([{genre: bot_joke_uk}]))  # друкування Анекдота українською
            case '2':
                lst_jokes_uk.clear()
                for _ in tqdm(range(5), desc="Переклад анекдотів"):
                    new_genre = get_random_item_func(lst_joke_genres)
                    bot_joke_en = get_joke_func(new_genre)  # отримання Анекдота
                    bot_joke_uk = GoogleTranslator(source='en', target='uk').translate(bot_joke_en)
                    temp_dict = {new_genre: bot_joke_uk}
                    lst_jokes_uk.append(temp_dict)
                print(display_joke_func(lst_jokes_uk))  # друкування Анекдота українською
            case '3':
                new_genre = get_random_item_func(lst_joke_genres)
                bot_joke_en = get_joke_func(new_genre)  # отримання Анекдота
                for _ in tqdm(range(2), desc="Переклад анекдоту"):
                    bot_joke_uk = GoogleTranslator(source='en', target='uk').translate(bot_joke_en)
                print(display_joke_func([{new_genre: bot_joke_uk}]))
            case _:
                print('Збігів не знайдено!')

        if not ask_continue_func(lst_names_uk[3], finish_section_text(lst_names_uk[3])):
            break
