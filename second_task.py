# Ф-ция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел)
# в качестве значения. Вычислить итоговую прибыль или убыток каждой компании
# Если все компании прибыльные, верните истину, если убыточная - ложь


dic_comp = {'intel':(1000, 3423, 423423, -10),
            'ibm':(100, 334_435_345_44, 678),
            'gigabait':(456, 55677, 56789)}

def get_sum_of_items(list):
    summa = 0
    for value in list:
        summa += value
    return summa

def get_plus_of_como(dicts_of_comp):
    redy = True
    for key, value in dicts_of_comp.items():
        if get_sum_of_items(value) < 0:
            return False
    return True
print(get_plus_of_como(dic_comp))
