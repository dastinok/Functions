# Программа банкомат


MIN = 0
MAX = 5
BALANCE = 0


def main():

    print('Добро пожаловать в программу Банкомат!')
    print('****************************************')
    print('Меню выбора опций:\n'
          '1. Пополнить\n'
          '2. Снять\n'
          '3. Показать баланс\n'
          '4. Выйти')
    choice = get_number(MIN, MAX)



    if choice.isdigit() and int(choice) == 1:
        depo = int(get_deposit())
        print(f'Вы внесли {depo:.2f} рублей')
        show_balance()
        main()
    elif choice.isdigit() and int(choice) == 2:
        withdraw = int(get_withdraw())
        print(f'Вы сняли {withdraw:.2f} рублей')
        show_balance()
        main()
    elif choice.isdigit() and int(choice) == 3:
        show_balance()
        main()
    else:
        print('До свидания!')
        quit()

def get_number(minim: int, maxim: int) -> int | str:
    while True:
        number = input('Введите номер опции: ')
        if number.isdigit() and minim < int(number) < maxim:
            return number


def get_deposit():
    global BALANCE
    while True:
        deposit = input('Введите сумму депозита (в рублях): ')
        if deposit.isdigit():
            BALANCE += int(deposit)
            return deposit

def get_withdraw():
    global BALANCE
    withdraw = input('Введите сумму снятия: ')
    if withdraw.isdigit() and int(withdraw) > BALANCE:
        print('Денег нет')
        main()
    else:
        BALANCE -= int(withdraw)
        return withdraw

def show_balance():
    print(f'**********************************')
    print(f'Ваш баланс = {BALANCE:.2f} рублей')
    print(f'**********************************')


if __name__ == '__main__':
    main()