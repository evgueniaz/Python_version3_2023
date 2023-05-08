# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате 
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Enter a sum of numbers to be guessed: "))
p = int(input("Enter a product of numbers to be guessed: "))
x = 1
y = s - x

while x * y != p and y > 0:
    x += 1
    y = s - x

    
if x > 0 and y > 0:
    print(f'The chosen numbers are {x} and {y}')
else:
    print(f'There are no natural solution.')
