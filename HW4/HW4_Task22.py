# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 
# числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input("Enter a natural number for the first list length >> "))
while n < 1:
    print(f"You've entered not a natural number.")
    n = int(input("Enter a natural number for a list length >> "))
m = int(input("Enter a natural number for the first list length >> "))
while n < 1:
    print(f"You've entered not a natural number.")
    m = int(input("Enter a natural number for a list length >> "))
rooster_1 = [random.randint(1, 20) for i in range(n)]
print(rooster_1)
rooster_2 = [random.randint(1, 20) for i in range(m)]
print(rooster_2)
common_elems = sorted(set(rooster_1).intersection(rooster_2))
if len(common_elems) == 0:
    print(f"There are no common elements!")
else:
    print(f"Common elements of the two sets are: ")
    print(*common_elems, sep=" ")


