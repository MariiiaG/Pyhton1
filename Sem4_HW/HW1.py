# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

nums1_len = int(input("Введите длину первого набора чисел : "))
nums2_len = int(input("Введите длину второго набора чисел : "))

nums1 = []
for i in range(nums1_len):
    nums1.append(randint(0, 20))
print(nums1)

nums2 = []
for i in range(nums2_len) :
    nums2.append(randint(0, 20))
print(nums2)

combined = set(nums1).union(set(nums2))
print(combined)

