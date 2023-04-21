# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input("Enter a natural number for a list length >> "))
while n < 1:
    print(f"You've entered not a natural number.")
    n = int(input("Enter a natural number for a list length >> "))
rooster = [random.randint(1, 20) for i in range(n)]
print(rooster)
x = int(input("Enter a number to be found in the list >> "))
resulting_set = set()
difference_set = []

for el in rooster:
    difference_set.append(abs(el - x))
min_difference = min(difference_set)
for i in range(n):
    if difference_set[i] == min_difference:
        resulting_set.add(rooster[i])
print(f'The closest number(s) to your number in the given set is (are): {resulting_set}')