

def get_num(min_val: int, max_val: int) -> int:
    while True:
        digit = input(f'Введите число от {min_val} до {max_val}: ')
        if digit.isdigit() and min_val < int(digit) < max_val:
            return int(digit)

a = get_num(0, 10)
print(a)
print(type(a))

