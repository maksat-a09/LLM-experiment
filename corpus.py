"""Корпус тестов для опыта 3.

Поля: id, group, lang, text.
group объединяет тексты с одинаковым смыслом на разных языках,
чтобы считать отношение к английскому внутри группы.

Важно: казахские и транслитерированные тексты составил Claude,
носитель языка их не проверял.
"""

TESTS = [
    # --- Группа short: короткая фраза на четырёх вариантах ---
    {"id": "short_en", "group": "short", "lang": "en",
     "text": "Connect the repository to this folder"},
    {"id": "short_ru", "group": "short", "lang": "ru",
     "text": "Подключи репозиторий к этой папке"},
    {"id": "short_ru_translit", "group": "short", "lang": "ru_translit",
     "text": "Podklyuchi repozitoriy k etoy papke"},
    {"id": "short_kk", "group": "short", "lang": "kk",
     "text": "Репозиторийді осы қалтаға қос"},

    # --- Группа paragraph: абзац из трёх предложений ---
    {"id": "paragraph_en", "group": "paragraph", "lang": "en",
     "text": "Tokens are pieces of text that a language model works with. "
             "A token can be a syllable, a word, or a punctuation mark. "
             "The more tokens a text has, the more it costs to process."},
    {"id": "paragraph_ru", "group": "paragraph", "lang": "ru",
     "text": "Токены — это кусочки текста, с которыми работает языковая модель. "
             "Токеном может быть слог, слово или знак препинания. "
             "Чем больше токенов в тексте, тем дороже его обработка."},
    {"id": "paragraph_ru_translit", "group": "paragraph", "lang": "ru_translit",
     "text": "Tokeny — eto kusochki teksta, s kotorymi rabotaet yazykovaya model. "
             "Tokenom mozhet byt slog, slovo ili znak prepinaniya. "
             "Chem bolshe tokenov v tekste, tem dorozhe ego obrabotka."},
    {"id": "paragraph_kk", "group": "paragraph", "lang": "kk",
     "text": "Токендер — тілдік модель жұмыс істейтін мәтін бөліктері. "
             "Токен буын, сөз немесе тыныс белгісі болуы мүмкін. "
             "Мәтінде токен неғұрлым көп болса, оны өңдеу соғұрлым қымбат."},

    # --- Группа greeting: бытовая фраза ---
    {"id": "greeting_en", "group": "greeting", "lang": "en",
     "text": "Good morning! How are you today?"},
    {"id": "greeting_ru", "group": "greeting", "lang": "ru",
     "text": "Доброе утро! Как у тебя дела сегодня?"},
    {"id": "greeting_ru_translit", "group": "greeting", "lang": "ru_translit",
     "text": "Dobroe utro! Kak u tebya dela segodnya?"},
    {"id": "greeting_kk", "group": "greeting", "lang": "kk",
     "text": "Қайырлы таң! Бүгін қалайсың?"},

    # --- Одиночные тесты без перевода (group = "single") ---
    # Буквы казахского алфавита, которых нет в русском
    {"id": "kk_letters", "group": "single", "lang": "kk",
     "text": "ә ғ қ ң ө ұ ү һ і"},
    # Те же буквы казахского алфавита в слове-примере
    {"id": "kk_word_qazaqstan", "group": "single", "lang": "kk",
     "text": "Қазақстан"},
    # Длинное русское слово
    {"id": "ru_long_word", "group": "single", "lang": "ru",
     "text": "Достопримечательность"},
    # Длинное английское слово
    {"id": "en_long_word", "group": "single", "lang": "en",
     "text": "Internationalization"},
    # Код
    {"id": "code_python", "group": "single", "lang": "code",
     "text": "def add(a, b):\n    return a + b\n\nprint(add(2, 3))"},
    # JSON
    {"id": "json", "group": "single", "lang": "code",
     "text": '{"name": "Maksat", "age": 30, "tags": ["llm", "tokens"]}'},
    # URL
    {"id": "url", "group": "single", "lang": "code",
     "text": "https://github.com/maksat-a09/LLM-experiment"},
    # Числа
    {"id": "numbers", "group": "single", "lang": "digits",
     "text": "3.14159265358979 1234567890 2026-11-10"},
    # Эмодзи и смешанный текст
    {"id": "emoji_mixed", "group": "single", "lang": "mixed",
     "text": "Привет! 👋 Hello! 🚀 Сәлем! 🙂"},
]
