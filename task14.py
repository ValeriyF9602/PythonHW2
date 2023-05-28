# Задача 14:

# Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.

#   10 -> 1 2 4 8


n = int(input('Введите число N: '))

if n < 1:
    print('Таких целых степеней двойки нет')
else:
    degree = 1
    result = 1
    flag = True

    while flag:
        print(result, end=' ')
        result = pow(2, degree)
        degree += 1
        if result > n:
            flag = False