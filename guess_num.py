# Угадай число. Ком угадывает

MIN = 1
MAX = 101

def get_number(minim: int, maxim: int) -> str:
    while True:
        number = input(f'Введите значение от {minim} до {maxim}: ')
        if number.isdigit() and minim < int(number) < maxim:
            return number



num = get_number(MIN, MAX)
numbers = list(range(1, 1001))
print(f'Вы загадали {num}')
print(type(num))

def find_number(lst: list, search: int) -> int:
    low = 0
    maxim = len(lst) - 1
    res = False

    while low <= maxim and not res:
        middle = (low + maxim) // 2
        guess = lst[middle]
        if guess == int(search):
            res = True
            return res
        if guess > int(search):
            maxim = middle - 1

        else:
            low = middle + 1
            print(low)
    return res


result = find_number(numbers, int(num))
print(result)
if result:
    print(f'Элемент найден {result}')
else:
    print('Элемент не найден')