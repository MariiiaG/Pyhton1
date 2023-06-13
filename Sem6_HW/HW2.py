# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
from random import randint


start = int(input("Первое число диапазона : "))
end = int(input("Последнее число диапазона : "))

my_list = []
for i in range (15):
    my_list.append(randint(1, 20))
    
print(my_list)

for i in range(len(my_list)) :
    if start <= my_list[i] <= end: 
        print(i)
        
