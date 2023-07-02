# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

while True:
    number = int(input('Введите число от 1 до 999 '))
    PRINT_NUMBER = number
    sum_of_number = 0
    reverse_of_number = 0
    if 0 < number < 1000:
        if number >= 100:
            print(f'Введено трехзначное число {PRINT_NUMBER}')
            while number > 0:
                dig = number % 10
                reverse_of_number = reverse_of_number * 10 + dig
                number //= 10
            print(f'Отражение числа {PRINT_NUMBER} - {reverse_of_number}')
            break
        elif 10 < number < 100:
            print(f'Введено двухзначное число {PRINT_NUMBER}')
            while number > 0:
                sum_of_number = number % 10 + sum_of_number
                number //= 10
            print(f'Сумма цифр числа {PRINT_NUMBER} равна {sum_of_number}')
            break
        else:
            print(f'Введена цифра {PRINT_NUMBER}')
            square = number**2
            print(f'Квадрат цифры {PRINT_NUMBER} равен {square}')
            break
    else:
        print('Введено неверное число!')
        continue
