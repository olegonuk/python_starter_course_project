"""Розділ Рекомендації"""
from data import list_recommendations_en as lst_names_en
from data import list_recommendations_uk as lst_names_uk
from utils.functions import display_header_func
from utils.functions import ask_continue_func
from utils.functions import finish_section_text
from recommendations.recom_films import ask_for_film as run_films
from recommendations.recom_music import ask_for_music as run_music
from recommendations.recom_games import ask_for_games as run_games


def ask_recommendations():
    """Функція зображення меню розділу Рекомендації"""
    while True:
        print(display_header_func(f'Section|{lst_names_en[5]}', 'fancy142'))

        user_subsection_choice = input(f"Розділ \"{lst_names_uk[5]}\":\n"
                                       "- Рекомендувати Фільми № 1\n"
                                       "- Рекомендувати Музику №2\n"
                                       "- Рекомендувати Ігри №3\n"
                                       "Введіть 'return' для повернення "
                                       "до Головного меню\n: ").lower()
        if user_subsection_choice == 'return':  # завершення програми комбінацією символів «return»
            break

        if user_subsection_choice not in ['1', '2', '3']:
            print('Ви ввели недійсне число. Будь ласка, введіть число від 1 до 3 або "return"')
            continue

        match user_subsection_choice:
            case '1':
                run_films()
            case '2':
                run_music()
            case '3':
                run_games()
            case _:
                print('Збігів не знайдено!')

        if not ask_continue_func(lst_names_uk[5], finish_section_text(lst_names_uk[5])):
            break
