# Напишите ф-цию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ значение переданного аргумента,
# а значение - имя аргумента. Если ключ не хешируем то используйте его строковое представление




def get_key(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        new_dict[v] = k
        if hash(k) is None:
            return str(k)

    return new_dict

a = get_key(first='234', fdds=3434, third='3435')
print(a)