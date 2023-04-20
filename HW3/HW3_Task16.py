# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
# -> 1

import random

n = int(input("Enter a natural number for a list length >> "))
rooster = [random.randint(1, 20) for i in range(n)]
print(rooster)
x = int(input("Enter a number to be found in the list >> "))
count = rooster.count(x)
print(f'Number {x} is repeated {count} times in the list.')

