# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def adding_two_nums(num_1: int, num_2: int) -> int:
    if num_2 == 0 or (num_1 == 0 and num_2 == 0):
        return num_1
    return adding_two_nums(num_1 + 1, num_2 - 1)

number_1 = int(input("Enter a non-negative number: "))
number_2 = int(input("Enter a non-negative number to be added to the first one: "))
print(f'{number_1} + {number_2} = {adding_two_nums(number_1, number_2)}')
