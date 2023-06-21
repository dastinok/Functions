# Напишите ф-цию, которая принимает строку текста
# Сформируйте список с уник кодами Юникод каждого символа

text = 'Тут должен быть текст)'

def get_sort_unicode(text: int) -> list:
    my_list = []
    for i in text:
        if ord(i) not in my_list:
            my_list.append(ord(i))
    my_list.sort()
    return my_list
print(get_sort_unicode(text))

