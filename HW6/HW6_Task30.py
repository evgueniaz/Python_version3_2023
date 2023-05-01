# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first_el_progression = int(input("Enter a value of the first element of the arithmetic progression: "))
common_diff = int(input("Enter a value of a common difference of the arithmetic progression: "))
amount_elems = int(input("Enter a number of elements of the arithmetic progression to be printed: "))

print([i for i in range(first_el_progression, 
                        first_el_progression + common_diff * (amount_elems - 1) + 1, common_diff)])

# res_progression = []

# def arithm_progression(u_1, d, n):
#     for i in range(1, n + 1):
#         res_progression.append(u_1 + d * (i - 1))
#     return res_progression


# print(arithm_progression(first_el_progression, common_diff, amount_elems))


# def arithm_progression_1(u_1, d, n):
#     res_progr = [u_1 + d * (i - 1) for i in range(1, n + 1)]
#     return res_progr


# print(arithm_progression_1(first_el_progression, common_diff, amount_elems))