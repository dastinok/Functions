# Функция получает на вход строку из 2 чисел.
# Сформир словарь ключ - символ Unicod, значение - целое число
# Диапазон пар ключ-значение от наименьшего до наибольшего


def create_dict():
    my_dict = {}
    start, end = map(int, input('Введите числа: ').split())
    if start < end:
        start, end = end, start
    for i in range(start, end + 1):
        my_dict[chr(i)] = i
    return my_dict
print(create_dict())


