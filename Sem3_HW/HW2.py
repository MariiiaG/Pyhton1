# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

length = int(input("Введите длину списка : "))
find_el = int(input("Введите число X : "))

my_list = []
for i in range(length):
    my_list.append(i)
print(my_list)

if find_el > my_list[-1] :
    print(my_list[-1])
        
else :
    for i in range(length):
        if find_el - my_list[i] == 1 :
            print(my_list[i])
        else :
            i += 1
