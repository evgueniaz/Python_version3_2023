# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

S = int(input("Введите число, кратное 6, которое соответствует общему количеству журавликов:  "))
while S % 6 != 0:
    num = int(input("Введите число, кратное 6:  "))
a = int(S / 6)
b = 4 * a

print(f"Петя, Катя и Сережа сделали соответственн {a}, {b} и {a} журавликов")
