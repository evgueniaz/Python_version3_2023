# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на
# грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на
# них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

n = int(input("Enter a natural number for the amount of blueberry bushes >> "))
while n < 1:
    print(f"You've entered not a natural number.")
    n = int(input("Enter a natural number for the amount of blueberry bushes >> "))
amounts_of_berries = [random.randint(10, 100) for i in range(n)]
print(amounts_of_berries)
picked_berries = []
for i in range(n - 2):
    picked_berries.append(amounts_of_berries[i] + amounts_of_berries[i+1] + amounts_of_berries[i+2])
picked_berries.append(amounts_of_berries[-2]+amounts_of_berries[-1]+amounts_of_berries[0])
picked_berries.append(amounts_of_berries[-1]+amounts_of_berries[0]+amounts_of_berries[1])
# print(picked_berries)
print(f"Maximum amount of berries that could be picked is: ")
print(max(picked_berries))
