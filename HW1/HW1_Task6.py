# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали 
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых 
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = int(input("Enter a 6-digit ticket number:  "))
while ticket > 1000000 or ticket < 99999:
    ticket = int(input("Enter a 6-digit ticket number:  "))
num1 = ticket % 1000
num2 = ticket // 1000
sum1 = 0
sum2 = 0
for i in range(3):
    sum1 += num1 % 10
    sum2 += num2 % 10
    num1 = num1 // 10
    num2 = num2 // 10
if sum1== sum2:
    print("You've got a lucky ticket!")
else:
    print("Sorry! Your ticket is not lucky.")