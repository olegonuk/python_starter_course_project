"""Розділ Рекомендації Фільми"""
from data import films as films_list
from data import list_recommendations_en as lst_names_en
from data import list_recommendations_uk as lst_names_uk
from utils.functions import display_header_func
from utils.functions import get_random_item_func
from utils.functions import get_genre_func
from utils.functions import filtered_lst_func
from utils.functions import list_items_func
from utils.functions import display_elem_func
from utils.functions import open_info_func
from utils.functions import ask_continue_func
from utils.functions import finish_recom_section_text

def ask_for_film():
    """Функція зображення меню розділу Фільми"""
    while True:
        print(display_header_func(f'Recommendations|{lst_names_en[0]}', 'fancy142'))

        user_subsection_choice = input(f"Розділ Рекомендації / \"{lst_names_uk[0]}\":\n"
                                       "- За жанром №1\n"
                                       "- Список фільмів №2\n"
                                       "- Випадковий фільм №3\n"
                                       "Введіть 'return' до попереднього меню\n: ").lower()
        if user_subsection_choice == 'return':  # до попереднього меню
            break

        if user_subsection_choice not in ['1', '2', '3']:
            print('Ви ввели недійсне число. Будь ласка, введіть число від 1 до 3 або "return"')
            continue

        match user_subsection_choice:
            case '1':
                genre = get_genre_func(films_list)
                print(list_items_func(filtered_lst_func(films_list, genre), lst_names_en[0]))
                open_info_func(filtered_lst_func(films_list, genre))
            case '2':
                print(list_items_func(films_list, lst_names_en[0]))
                open_info_func(films_list)
            case '3':
                print(display_elem_func(get_random_item_func(films_list)))
            case _:
                print('Збігів не знайдено!')

        if not ask_continue_func(lst_names_uk[0], finish_recom_section_text(lst_names_uk[0])):
            break
