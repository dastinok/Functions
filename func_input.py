

def get_str() -> str:
    word = input('Введите слово: ')
    if word.isalpha():
        return word
    if word.isdigit():
        return get_str()


string = get_str()
print(string)