# Максимальное число

def max_num(a: int, b: int) -> int:
    return a if a > b else b


a, b, z = 10, 18, 26
number = max_num(a, (max_num(b, z)))
print(number)

