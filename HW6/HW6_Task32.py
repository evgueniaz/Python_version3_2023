# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input("Enter a natural number for a list length >> "))
while n < 1:
    print(f"You've entered not a natural number.")
    n = int(input("Enter a natural number for the first list length >> "))

rooster = [random.randint(-20, 20) for i in range(n)]
print(rooster)

low_limit = int(input("Enter a whole number for a lower limit of a searched interval >> "))
upper_limit = int(input("Enter a whole number for an upper limit of a searched interval >> "))

print([i for i in range(n) if low_limit <= rooster[i] <= upper_limit])
