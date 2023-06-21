from typing import Any

def check_type(something: Any) -> int | str | bool:
    if isinstance(something, int):
        return something*10
    elif isinstance(something, str):
        return something + '- строка'
    else:
        return False

print(check_type(5))
print(check_type('Слово'))
print(check_type(['Слово', 'Словечко']))
