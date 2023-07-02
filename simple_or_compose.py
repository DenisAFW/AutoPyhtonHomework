# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

min_limit = 0
max_limit = 100000
SIMPLE = 2
count = 0
divider = 1
while True:
    number = int(input('Введите число '))
    if min_limit < number < max_limit:
        while divider != number + 1:
            if number % divider == 0:
                count += 1
                divider += 1
            else:
                divider += 1
        if count > SIMPLE:
            print('Число является составным')
            break
        else:
            print('Число является простым')
            break
    else:
        print("Введено неверное число")