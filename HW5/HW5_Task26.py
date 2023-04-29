# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в 
# целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def whole_number_powering (base: int, exponent: int) -> int:
    if exponent != 0:
        return base * whole_number_powering(base, exponent-1)
    return 1

base_to_use = int(input("Enter a whole number to be powered: "))
power = int(input("Enter a whole number to be used as an exponent: "))
print(f'{base_to_use} elevated to the power of {power} equals {whole_number_powering(base_to_use, power)}')
