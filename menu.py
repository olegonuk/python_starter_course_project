"""Головне меню Чат-боту"""
from recommendations.menu_recommendations import ask_recommendations as run_recommendations
from jokes.jokes import ask_for_joke as run_joke
from stories.stories import ask_for_story as run_story
from games.rock_paper_scissors_game import ask_user_move as play_r_p_s
from games.guess_number import ask_user_number as play_guess_number
from utils.functions import display_header_func
from utils.functions import exit_program_func


def main_menu():
    """Функція зображення Головного Меню"""
    while True:
        print(display_header_func('Welcome to the Chat-bot', 'tarty4'))

        var_user_choice = input("\nГоловне меню:\n"
                                "- Рекомендації (фільми/музика/ігри) № 1\n"
                                "- Анекдот №2\n"
                                "- Історії №3\n"
                                "- Ігри: Камінь-Ножиці-Папір №4\n"
                                "- Ігри: Вгадай число №5\n"
                                "Введіть 'exit' для виходу з програми\n: ").strip().lower()

        if var_user_choice == 'exit':  # завершення програми «exit»
            print(exit_program_func())
            break

        if var_user_choice not in ['1', '2', '3', '4', '5']:
            print('Ви ввели недійсне число! Будь ласка, введіть число від 1 до 5 або "exit"!')
            continue

        match var_user_choice:
            case '1':
                run_recommendations()
            case '2':
                run_joke()
            case '3':
                run_story()
            case '4':
                play_r_p_s()
            case '5':
                play_guess_number()
            case _:
                print('Збігів не знайдено!')
