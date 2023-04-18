# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть


import random

n = int(input("Enter a number of coins that lay on a table: "))
set_of_coins = []
for i in range(n):
    set_of_coins.append(random.randint(0, 1))
print(set_of_coins, end=" ")

tails = 0
heads = 0
for el in set_of_coins:
    if el == 0:
        tails += 1
    else:
        heads += 1
if heads > tails:
    print (f'\n Minimal number of coins to be turned is {tails}')
else:
    print (f'\n Minimal number of coins to be turned is {heads}')
    
