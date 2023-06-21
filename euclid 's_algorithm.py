import time


def get_nud(a: int, b: int) -> int:
    """Вычисляется НОД для натуральных чисел a и b
        по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a

def test_nod(func):
    # --- тест№1---
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('Тест №1 - ОК')
    else:
        print('Тест - Fail')

    # --- Тест №2----

    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('Тест №2 - ОК')
    else:
        print('Тест №2 - Fail')

    # --- Тест №3----
    a = 2
    b = 1000000000
    st = time.time()
    res = func(a,b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('Тест №3 - ОК')
    else:
        print('Тест №3 - Fail')

#res = get_nud(18, 24)
#print(res)
#help(get_nud)

test_nod(get_nud)