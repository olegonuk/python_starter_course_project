"""Розділ Рекомендації Музика"""
from data import music as music_list
from data import list_recommendations_en as lst_names_en
from data import list_recommendations_uk as lst_names_uk
from utils.functions import display_header_func
from utils.functions import get_random_item_func
from utils.functions import get_genre_func
from utils.functions import list_items_func
from utils.functions import filtered_lst_func
from utils.functions import display_elem_func
from utils.functions import open_info_func
from utils.functions import ask_continue_func
from utils.functions import finish_recom_section_text

def ask_for_music():
    """Функція зображення меню розділу Музика"""
    while True:
        print(display_header_func(f'Recommendations|{lst_names_en[1]}', 'fancy142'))

        user_subsection_choice = input(f"Розділ Рекомендації / \"{lst_names_uk[1]}\":\n"
                                       "- За жанром №1\n"
                                       "- Список Пісень №2\n"
                                       "- Випадкова пісня №3\n"
                                       "Введіть 'return' до попереднього меню\n: ").lower()
        if user_subsection_choice == 'return':  # до попереднього меню
            break

        if user_subsection_choice not in ['1', '2', '3']:
            print('Ви ввели недійсне число. Будь ласка, введіть число від 1 до 3 або "return"')
            continue

        match user_subsection_choice:
            case '1':
                genre = get_genre_func(music_list)  # отримання випадкового елемента
                print(list_items_func(filtered_lst_func(music_list, genre), lst_names_en[1]))
                open_info_func(filtered_lst_func(music_list, genre))
            case '2':
                print(list_items_func(music_list, lst_names_en[1]))  # друкування списку елементів
                open_info_func(music_list)
            case '3':
                print(display_elem_func(get_random_item_func(music_list)))  # друкування
            case _:
                print('Збігів не знайдено!')

        if not ask_continue_func(lst_names_uk[1], finish_recom_section_text(lst_names_uk[1])):
            break
