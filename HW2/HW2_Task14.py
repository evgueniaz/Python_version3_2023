# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Enter a positive integer:  "))
while n < 1:
    n = int(input("You entered a negative number. Please give a positive one:  "))
i = 0
while 2 ** i <= n:
    print(2 ** i, end=" ")
    i += 1
