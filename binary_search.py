

def binary_search(lst: list, search: int):
    low = 0
    max = len(lst) - 1
    res = False

    while low <= max and not res:
        middle = (low + max) // 2
        guess = lst[middle]
        if guess == search:
            res = True
            return res
        if guess > search:
            max = middle - 1
        else:
            low = middle + 1
    return res

lst = list(range(1, 1001))

print(lst)
print(type(lst))
value = 56
result = binary_search(lst, value)
if result:
    print('Элемент найден')
else:
    print('Элемент не найден')