# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите максимальную степень : "))
pow = 1
seq = 1

while pow <= n :
    seq *= 2
    pow += 1
    print(seq)