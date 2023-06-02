# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#  5
#     1 2 3 4 5
#     3
#     -> 1

import random
from random import randint

length = int(input("Введите количество элементов : "))
findnum = int(input("Введите число X : "))

my_list = []
for i in range(length) :
    my_list.append(random.randint(0,10))
print(my_list)

count = 0

for i in range(length):
    if my_list[i] == findnum :
        count += 1
print(count)

