# Фун-ция получает на вход список чисел. Отсортируйте его элементы in place
# Соритровка пузырьком.

my_list = [5, 1, 45, 6, 89, 4, 77, 87]
print(my_list)
def get_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                #temp = my_list[j]
                #my_list[j] = my_list[j + 1]
                #my_list[j + 1] = temp

get_sort(my_list)
print(my_list)