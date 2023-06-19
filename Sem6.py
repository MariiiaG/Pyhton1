# Тернарные операторы(Ternary operators). 
# Ternary operators evaluate something based on a condition being true or false. 
# It allows testing a condition in a single line replacing the multiline if-else making the code compact.
# condition_if_true if condition else condition_if_false

# a = 15
# b = 10 
# print(a if a < b else b) # 10 (example of using if within a print clause)


# Даны два списка чисел. Требуется вывести тк элементы первого списка 
# (в том порядке в котором они идут в первом списке), которых нет во втором списке 

# from random import randint

# list1 = [randint(0, 10) for i in range(15)]
# list2 = [randint(0, 10) for i in range(5)]
# final_list = []
# for i in list1 :
#     if i not in list2 :
#         final_list.append(i)
# print(list1)
# print(list2)
# print(final_list)

# import random
# print(f_list := [random.randint(0, 10) for _ in range (10)])
# print(s_list := [random.randint(0, 10) for _ in range (5)])
# ## print(f_list, s_list, sep='\n') 
# print([item for item in f_list if item not in s_list])


# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество
# элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного

# from random import randint

# my_list = [randint(0, 10) for _ in range(15)]
# count = 0 
# for i in range(1, len(my_list) - 1):
#     if my_list[i-1] < my_list[i] > my_list[i + 1]:
#         count += 1
# if my_list[-1] < my_list[0] > my_list[1]:
#     count += 1
# elif my_list[0] < my_list[-1] > my_list[-2]:
#     count += 1
# print(my_list, count, sep='\n')


# import random
# print(my_list := [random.randint(0, 10) for _ in range(10)])
# count = 0
# for i in range(len(my_list)):
#     if my_list[(i - 1) % len(my_list)] < my_list[i % len(my_list)] > my_list[(i + 1) % len(my_list)] : # см пример ниже
#         count += 1
# print(count)


# import random
# print(my_list := [random.randint(0, 10) for _ in range(10)])
# for i in range(100):
#     print(my_list[i % len(my_list)]) # зациклится и будет повторять элементы цикла по кругу



# Дан список чисел. Посчитайте: сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать

# from random import randint
# print(my_list := [randint(0, 5) for _ in range (10)])
# count = 0
# for i in set(my_list):
#     count += my_list.count(i) // 2
# print(count)


# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284

# sum_div_num = {}
# for number in range(1, 10000):
#     sum_ = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             sum_ += 1
#     sum_div_num[number] = sum_

# for num in sum_div_num:
#     if num == sum_div_num.get(sum_div_num.get(num)) and num > sum_div_num.get(num):
#         print(num, sum_div_num.get(num))