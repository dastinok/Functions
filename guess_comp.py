# Угадай число

MIN = 1
MAX = 100


def make_number(minim: int, maxim: int) -> int:
    number = input(f'Загадайте число от {minim} до {maxim}: ')
    if number.isdigit() and minim < int(number) < maxim:
        return int(number)

a = make_number(MIN, MAX)
print(a)