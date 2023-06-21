# Ф-ция на вход список чисел и два индекса. Вернуть сумму чисел
# между переданными индексами
# Если индекс выходит за пределы списка, сумма считается до конца и начала списка

def get_of_nums(list_of_number, start, end):
    if start < 0:
        start = 0
    if start > len(list_of_number):
        return None

    return sum(list_of_number[start+1:end])

print(get_of_nums([1,33,0,-345565,9], -1, 15))