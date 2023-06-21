# Напишите ф-цию которая принимает строку текста.
# Вывести ф-цие каждое слово с новой строки. Строки нумер с единицы
# Слова выводятся осортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю

text = 'Тут какой-то текст'

def get_word(text: str):
    text = text.lower().split()
    max_ = len(max(text, key=len))
    text.sort()
    for i, el in enumerate(text, 1):
        print(f'{i} {el:{max_}}')

get_word(text)
