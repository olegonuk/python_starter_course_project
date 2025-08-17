"""Розділ Історії"""
from tqdm import tqdm
from prettytable.colortable import ColorTable, Themes
from deep_translator import GoogleTranslator
from utils.functions import display_header_func
from utils.functions import get_random_item_func
from utils.functions import ask_continue_func
from utils.functions import finish_section_text
from data import stories_en as stories_list
from data import list_recommendations_en as lst_names_en
from data import list_recommendations_uk as lst_names_uk



def list_title_func(lst):
    """Функція друкування заголовків Історії"""
    return ("Список заголовків:\n" +
            "\n".join(f'{num}: {title}' for num, (title, _) in enumerate(lst, start=1)))


def display_story_func(lst):
    """Функція друкування Історії"""
    table = ColorTable(theme=Themes.PASTEL)
    table.align = 'l'
    table.field_names = ['№', 'Заголовок', 'Історія']
    table.max_width = 120
    for num, (title_story, text_story) in enumerate(lst, start=1):
        table.add_row([num, f"{title_story}", f"{text_story}"])
    return table


def ask_for_story():
    """Функція зображення меню розділу Історії"""
    while True:
        print(display_header_func(f'Section|{lst_names_en[4]}', 'fancy142'))

        user_subsection_choice = input(f"Розділ \"{lst_names_uk[4]}\":\n"
                                       "- Випадкова історія № 1\n"
                                       "- Перелік заголовків №2\n"
                                       "Введіть 'return' для повернення до Головного меню\n"
                                       ": ").lower()
        if user_subsection_choice == 'return':  # завершення програми комбінацією символів «return»
            break

        if user_subsection_choice not in ['1', '2']:
            print('Ви ввели недійсне число! Будь ласка, введіть число 1, 2 або "return"')
            continue

        match user_subsection_choice:
            case '1':
                title_story_en, text_story_en  = get_random_item_func(stories_list)
                for _ in tqdm(range(2), desc="Переклад історії"):
                    text_story_uk = GoogleTranslator(
                        source='en', target='uk').translate(text_story_en)
                print(display_story_func([(title_story_en, text_story_uk)]))
            case '2':
                print(list_title_func(stories_list))
                while True:
                    story_number = input("\nВведіть номер історії, яку хочете прочитати: ")
                    try:
                        story_number = int(story_number)
                        if 0 < story_number <= len(stories_list):
                            title_story_en, text_story_en = stories_list[story_number - 1]
                            for _ in tqdm(range(2), desc="Переклад історії"):
                                text_story_uk = GoogleTranslator(
                                    source='en', target='uk').translate(text_story_en)
                            print(display_story_func([(title_story_en, text_story_uk)]))
                            break
                    except ValueError:
                        print("Будь ласка, введіть коректний номер!")
            case _:
                print('Збігів не знайдено!')

        if not ask_continue_func(lst_names_uk[4], finish_section_text(lst_names_uk[4])):
            break
