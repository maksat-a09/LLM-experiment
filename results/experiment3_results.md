# Опыт 3. Результаты

Числа Claude — сырой `input_tokens` из `count_tokens`; в него входят накладные расходы на обёртку сообщения (см. строку `overhead`). Для сравнения языков они вычтены в таблицах отношений.

| id | символов | байт | tk:cl100k_base | tk:o200k_base |
|---|---|---|---|---|
| short_en | 37 | 37 | 6 | 6 |
| short_ru | 33 | 62 | 16 | 11 |
| short_ru_translit | 35 | 35 | 13 | 13 |
| short_kk | 29 | 55 | 22 | 11 |
| paragraph_en | 175 | 175 | 42 | 42 |
| paragraph_ru | 172 | 313 | 70 | 49 |
| paragraph_ru_translit | 177 | 179 | 62 | 56 |
| paragraph_kk | 168 | 308 | 133 | 55 |
| greeting_en | 32 | 32 | 8 | 8 |
| greeting_ru | 37 | 66 | 22 | 12 |
| greeting_ru_translit | 39 | 39 | 16 | 14 |
| greeting_kk | 28 | 51 | 27 | 13 |
| kk_letters | 17 | 26 | 24 | 9 |
| kk_word_qazaqstan | 9 | 18 | 7 | 1 |
| ru_long_word | 21 | 42 | 8 | 6 |
| en_long_word | 20 | 20 | 2 | 2 |
| code_python | 49 | 49 | 20 | 20 |
| json | 56 | 56 | 24 | 25 |
| url | 44 | 44 | 14 | 14 |
| numbers | 38 | 38 | 19 | 19 |
| emoji_mixed | 27 | 47 | 17 | 14 |
| overhead |  |  |  |  |

## Отношение к английскому (токены языка / токены en), накладные расходы вычтены

| группа | язык | tk:cl100k_base | tk:o200k_base |
|---|---|---|---|
| short | ru | 2.67 | 1.83 |
| short | ru_translit | 2.17 | 2.17 |
| short | kk | 3.67 | 1.83 |
| paragraph | ru | 1.67 | 1.17 |
| paragraph | ru_translit | 1.48 | 1.33 |
| paragraph | kk | 3.17 | 1.31 |
| greeting | ru | 2.75 | 1.50 |
| greeting | ru_translit | 2.00 | 1.75 |
| greeting | kk | 3.38 | 1.62 |
