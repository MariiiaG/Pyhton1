# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

base = int(input("Введите число - основание : ")) 
pow = int(input("Введите число - степень : "))

def math_power(base, pow):
    if pow == 0:
        return 1
    return math_power(base, pow - 1) * base

print(f"Число {base} в степени {pow} будет равно {math_power(base, pow)}")
    