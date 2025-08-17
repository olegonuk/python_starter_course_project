"""База даних"""
films = [
    {"title": "Dune: Part Two",
     "genre": "sci-fi",
     "why": "Епічне продовження культової історії про Арракіс."},
    {"title": "Coco",
     "genre": "animation",
     "why": "Зворушлива історія про пам’ять і сім’ю."},
    {"title": "Interstellar",
     "genre": "sci-fi",
     "why": "Мандрівка крізь час і простір заради любові та науки."},
    {"title": "Oppenheimer",
     "genre": "drama",
     "why": "Могутня біографія батька атомної бомби від Крістофера Нолана."},
    {"title": "The Shawshank Redemption",
     "genre": "drama",
     "why": "Найкраща історія про надію та дружбу."},
    {"title": "Everything Everywhere All at Once",
     "genre": "sci-fi",
     "why": "Абсурд, філософія і серце в кожній сцені."},
    {"title": "Spider-Man: Across the Spider-Verse",
     "genre": "animation",
     "why": "Візуальна революція в анімації."},
    {"title": "Poor Things",
     "genre": "drama",
     "why": "Естетика, сюр і емансипація в одному флаконі."},
    {"title": "Toy Story",
     "genre": "animation",
     "why": "Класика Pixar, яка відкрила нову еру мультиплікації."}
]

music = [
    {"author": "Dua Lipa",
     "title": "Houdini",
     "genre": "pop",
     "why": "Яскравий танцювальний хіт із диско-нотами."},
    {"author": "The Weeknd",
     "title": "Popular",
     "genre": "r&b",
     "why": "Атмосферний трек із серіалу 'The Idol'."},
    {"author": "John Williams",
     "title": "Star Wars Theme",
     "genre": "soundtrack",
     "why": "Ікона кіномузики."},
    {"author": "Taylor Swift",
     "title": "Anti-Hero",
     "genre": "pop",
     "why": "Іронічно й особисто про власні страхи."},
    {"author": "Olivia Rodrigo",
     "title": "vampire",
     "genre": "pop/rock",
     "why": "Емоційна драма в музичному форматі."},
    {"author": "Billie Eilish",
     "title": "bad guy",
     "genre": "pop",
     "why": "Мінімалістичний, але гіпнотичний трек."},
    {"author": "SZA",
     "title": "Kill Bill",
     "genre": "r&b",
     "why": "Соул із темною ліричною історією."},
    {"author": "Frank Ocean",
     "title": "Pink + White",
     "genre": "r&b",
     "why": "Ніжний і атмосферний трек."},
    {"author": "Hans Zimmer",
     "title": "Dune: Part Two OST",
     "genre": "soundtrack",
     "why": "Монументальний саундтрек до космічної саги."}
]

games = [
    {"title": "Alan Wake 2",
     "genre": "thriller/horror",
     "why": "Стильний психологічний жах із сильним сюжетом."},
    {"title": "The Witcher 3: Wild Hunt",
     "genre": "rpg",
     "why": "Майстерна історія та величезний відкритий світ."},
    {"title": "Uncharted 4",
     "genre": "adventure",
     "why": "Пригоди з кінематографічним розмахом."},
    {"title": "Elden Ring",
     "genre": "rpg",
     "why": "Темне фентезі від FromSoftware у відкритому світі."},
    {"title": "Baldur’s Gate 3",
     "genre": "rpg",
     "why": "Величезна свобода вибору і відмінна історія."},
    {"title": "The Legend of Zelda: Tears of the Kingdom",
     "genre": "adventure",
     "why": "Свобода дослідження і творчі механіки."},
    {"title": "Tomb Raider",
     "genre": "adventure",
     "why": "Класичні пригоди Лари Крофт."},
    {"title": "Resident Evil 4 Remake",
     "genre": "thriller/horror",
     "why": "Оновлена класика з новим рівнем страху."}
]

stories_uk = [
    (
        "Натхнення",
        "Кілька років тому молодий розробник працював над монотонним завданням — "
        "кожного дня вручну обробляв сотні файлів. "
        "Одного вечора, залишившись після роботи, він вирішив написати скрипт, "
        "який усе робив автоматично. "
        "На ранок завдання, яке раніше займало півдня, виконувалося за 3 хвилини. "
        "Керівництво було настільки вражене, що не тільки підвищило йому зарплату, а й "
        "зробило його наставником для новачків. "
        "Тепер його маленький вечірній експеримент став частиною внутрішніх інструментів компанії."
    ),
    (
        "Команда",
        "Був один проєкт із нереальним дедлайном — залишалося всього 5 днів, а зроблено "
        "було лише 60% роботи. "
        "Кожен у команді розумів, що шансів мало, але ніхто не опустив руки. "
        "Вони організували щоденні короткі стендапи, ділилися кодом у реальному часі та "
        "робили взаємні рев'ю навіть о другій ночі. "
        "Коли настав день здачі, вони вклалися у термін, і замовник сказав, що це «найкращий "
        "реліз, який вони бачили». "
        "Після цього вся команда зібралася разом на маленьке свято з піцою, і кожен відчув: "
        "разом вони можуть усе."
    ),
    (
        "Кумедний баг",
        "Під час роботи над новим вебсайтом замовник постійно скаржився, що форма входу "
        "«не працює». Розробники перевіряли код, сервери, бази даних — усе було ідеально. "
        "Виявилося, що проблема полягала у звичайній друкарській помилці: змінна для "
        "пароля у коді була названа 'passwrod' замість 'password'. "
        "Коли це з'ясувалося, вся команда сміялася хвилин п'ятнадцять, а цей випадок "
        "потрапив у внутрішній список «легендарних багів». "
        "З того часу вони ввели нове правило — завжди перевіряти орфографію навіть "
        "у назвах змінних."
    ),
    (
        "Фріланс",
        "Молодий фрілансер отримав замовлення зробити сайт для маленької кав’ярні. "
        "Спочатку він думав просто створити стандартний шаблон, але вирішив додати інтерактивну "
        "мапу, історії про кожен сорт кави та фото процесу обсмажування зерен. "
        "Коли сайт запустили, відвідуваність кав’ярні зросла вдвічі, і власники замовили у нього "
        "ще й мобільний додаток. "
        "Тепер цей фрілансер співпрацює з кількома кав’ярнями, а той перший сайт досі лишається "
        "його улюбленим проєктом."
    ),
    (
        "Хакатон",
        "На хакатоні команда студентів вирішила створити застосунок для пошуку загублених речей "
        "у гуртожитку. "
        "За 48 годин вони зробили прототип із фото-розпізнаванням та push-сповіщеннями. "
        "Хоча додаток ще був сирим, його презентували так весело і харизматично, що журі "
        "віддало їм перше місце. "
        "Пізніше вони доопрацювали продукт, і тепер його використовують не тільки в їхньому "
        "гуртожитку, а й у трьох університетах міста."
    )
]
stories_en = [
    (
        "Inspiration",
        "A few years ago, a young developer was working on a monotonous task — manually "
        "processing hundreds of files every day. One evening, staying late at work, he "
        "decided to write a script that would automate the entire process. "
        "By morning, the task that used to take half a day was completed in just 3 minutes. "
        "Management was so impressed that they not only gave him a raise but also made him "
        "a mentor for newcomers. Now his little evening experiment has become part of the "
        "company's internal tools."
    ),
    (
        "Teamwork",
        "There was a project with an impossible deadline — only 5 days left, and only 60% of "
        "the work was done. Everyone on the team knew the chances were slim, but no one "
        "gave up. They organized short daily stand-ups, shared code in real time, and did "
        "mutual code reviews even at 2 a.m. When the delivery day came, they met the deadline, "
        "and the client said it was 'the best release they had ever seen. After that, the whole "
        "team gathered for a small pizza celebration, and everyone felt: together, they could "
        "achieve anything."
    ),
    (
        "Funny Bug",
        "While working on a new website, the client constantly complained that the login form"
        " 'wasn’t working. The developers checked the code, the servers, the databases — "
        "everything was perfect. It turned out the problem was a simple typo: the password variable"
        " in the code was named 'passwrod' instead of 'password.' When this was discovered, the "
        "whole team laughed for about fifteen minutes, and the case went into the internal list "
        "of 'legendary bugs.' Since then, they adopted a new rule — always check spelling, even "
        "in variable names."
    ),
    (
        "Freelance",
        "A young freelancer got an order to create a website for a small coffee shop. "
        "At first, he thought of just using a standard template, but he decided to add an "
        "interactive map, stories about each coffee variety, and photos of the roasting process. "
        "When the website launched, the coffee shop's traffic doubled, and the owners also "
        "commissioned him to make a mobile app. Now this freelancer works with several coffee "
        "shops, and that first website remains his favorite project."
    ),
    (
        "Hackathon",
        "At a hackathon, a team of students decided to create an app for finding lost items "
        "in the dormitory. Within 48 hours, they built a prototype with photo recognition and "
        "push notifications. Although the app was still raw, they presented it so fun and "
        "charismatically that the jury awarded them first place. Later, they refined the product, "
        "and now it is used not only in their dorm but also in three universities across the city."
    )
]
list_recommendations_uk = ["Фільми", "Музика", "Ігри", "Анекдот", "Історії", "Рекомендації"]
list_recommendations_en = ["Films", "Music", "Games", "Jokes", "Stories", "Recommendations"]
list_finish_game_text = ["Камінь-Ножиці-Папір", "Вгадай число"]
list_greeting_game_text = ["Welcome to the: Rock-Scissors-Paper",
                           "Welcome to the game: Guess Number between 1 and 20"]
list_jokes_genres = [
    {"genre": "neutral"},
    {"genre": "chuck"},
    {"genre": "all"},
]
