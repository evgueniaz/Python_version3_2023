# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


num = int(input("Введите трехзначное число:  "))
while num < 100 or num > 999:
    num = int(input("Введите трехзначное число:  "))
sum = 0
for i in range (3):
    sum += num % 10
    num = num // 10

print(f"Сумма цифр Вашего числа равна {sum}")
