# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

num1 = int(input("Введите первое число : "))
num2 = int(input("Введите второе число : "))

def plus (num1, num2):
    if num2 == 0:
        return num1
    return plus(num1 + 1, num2 - 1)

print(plus(num1, num2))