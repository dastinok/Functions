

def whore(price: float = 300) -> str:
    if price == 300:
        return 'Сам соси'
    if price > 3000:
        return 'Групповушка'
    elif 1000 < price <= 3000:
        return 'Только один'
    else:
        return 'Омлет'

print(whore(2500))
print(whore())

