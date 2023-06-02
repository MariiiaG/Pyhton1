# Задачв 17. Дан список чисел. Определить, сколько в нем встречается различных чисел

# import random
# from random import randint

# my_list = []
# for _ in range(10) :
#     my_list.append(random.randint(0, 10))
# print(my_list)

# # 1-й вариант. Превратим список в множество, чтобы избавиться от повторяющихся элементов
# # my_list = set(my_list) 
# # print(my_list)
# # print(len(my_list))

# # 2-й вариант методом перебора
# uniq_list = []
# for item in my_list :
#     if item not in uniq_list :
#         uniq_list.append(item)
# print(uniq_list)
# print(len(uniq_list))


# my_string = "hfsjkdqwiudkjask"
# print(my_string) # hfsjkdqwiudkjask
# my_string = list(my_string) # ['h', 'f', 's', 'j', 'k', 'd', 'q', 'w', 'i', 'u', 'd', 'k', 'j', 'a', 's', 'k']
# print(my_string)



# Задача 19. Дана последовательность из N целых чисел и число К.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо. 
# К - положительное число

# from random import randint

# my_list = list()
# length = int(input("How long is the list ? "))
# for i in range(length) :
#     my_list.append(randint(0, 10))
# print(my_list)
# k = int(input("After which element is the break ?"))
# for i in range(k) :
#     my_list.insert(0, my_list.pop())
# print(my_list)


# Задача 21. Напишите программу для печати всех уникальных значений в словаре

# my_dict = [{"V": "S001"}, 
#            {"V": "S002"}, 
#            {"VI": "S001"}, 
#            {"VI": "S005"}, 
#            {"VII": "S005"}, 
#            {"V": "S009"}, 
#            {"VIII": "S007"}]
# # my_list = []
# # for i in range(len(my_dict)) :
# #     my_list += my_dict[i].values()
# # print(set(my_list))

# new_list = [] # alternative solution
# for item in my_dict:
#     for values in item.values():
#         new_list.append(values)
# print(set(new_list))


# Задача 23: Дан список, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего 
# (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] 
# Output: 2 (-1 < 5, 2 < 3)

# from random import randint

# num = int(input("Введите длину списка : "))
# my_list = []
# for i in range(num) :
#     my_list.append(randint(-5, 10))
# print(my_list)
# count = 0
# for i in range(len(my_list) - 1) :
#     if my_list[i + 1] > my_list[i]:
#         count += 1
# print(count)