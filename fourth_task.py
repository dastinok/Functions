# Ф-ция принимает на вход три списка одинаковой длины:
# имена, ставка, премия с указанием процентов вида 00.00%
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значений
# Сумма рассчитывается как ставка умнож на процент премии

def get_lst_premia(list_of_names: list[str], list_stavka: list[int], list_premia: list[str]):
    #len(1) == len(2) == len(3)
    dict_of_premia = {}
    for index, name in enumerate(list_of_names):
        dict_of_premia[name] = list_stavka[index] * (float(list_premia[index][0:-1]) + 100) / 100
    return dict_of_premia

names = ['test1', 'test2', 'test3']
stavca = [1000,2000,3000]
percents = ['10.23%','10.23%','10.23%']

print(get_lst_premia(names,stavca,percents))