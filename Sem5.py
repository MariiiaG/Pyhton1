# Найти N-е число Фибоначчи. 
# a0 = 0 a1 = 1 ak = ak-1 + ak-2

# fib = int(input("Введите номер числа в последовательности Фибоначчи : "))

# def fibo(number: int) -> int:
#     if number in [0, 1]:
#         return number
#     return fibo(number - 1) + fibo(number - 2)
    
# print(fibo(fib))


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные 
# Напишите программу, которая заменяет оценки Василия, но наоборот: максимaльные - на минимальные 

# import random
# from random import randint

# grades = []
# for _ in range (10) :
#     grades.append(randint(1, 5))
# print(grades)
    
# for i in range(len(grades)):
#     if grades[i] == 5 :
#         grades[i] = 1
# print(grades)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. 
# Простое число - число, которое имеет 2 делителя : 1 и n (само число)


# def simple(num):
#     count = 0 
#     for i in range(1, num+1):
#         if num % i == 0 :
#             count += 1
#     if count == 2 :
#             return(f"Число {num} простое")
#     return(f"Число {num} составное")
# print(simple(int(input("Введите число : "))))


# def is_simple (num: int) -> bool:
#     if num in [1, 2]:
#         return True
#     for i in range (3, num // 2 + 1, 2): # с шагом 2, т.к все чётные числа - составные (делятся на 1 и 2)
#         if num % i == 0 :
#             return False
#     return True
# print(is_simple(int(input("Введите число : "))))


# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Запрещается вводить массивы и использовать циклы

def sequence(length):
    if length == 0:
        return ""
    variable = input("Введите число : ")
    return sequence(length - 1) + variable + " "
print(sequence(5))








# На вход поступает число. Нужно найти сумму его чисел, если сумма чисел больше 10, 
# то найти сумму чисел получившегося числа и так до тех пор пока сумма чисел не будет меньше 10

# num = int(input("Введите число : "))

# def 