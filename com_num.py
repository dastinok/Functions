# Угадай число

import random

MIN = 0
MAX = 1000
def get_random(minim: int, maxim: int) -> int:
    first = random.randrange(minim, maxim)
    return first

num = get_random(MIN, MAX)
print(f'Комп загадал число - {num}')
#print(type(num))


def get_effort(comp: int) -> int | str:
    effort = 10
    while effort > 0:

        human = input('Введите число: ')

        if human.isdigit() and int(human) == comp:
            return int(human)

        if human.isdigit() and int(human) > comp:
            print('Ваше число больше')

        elif human.isdigit() and int(human) < comp:
            print('Ваше число меньше')
        effort -= 1
    else:
        exit('Вы проиграли! ((( Попытки закончились')



answer = get_effort(num)
print(f'Угадали - {answer}')




