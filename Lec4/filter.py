# Функция filter

# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта 
# и возвращает итератор с теми объектами, для которых функция вернула True.

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x : x % 10 == 5, data))
# print(res) # [15, 65, 175] filtered out only those elements that ended with 5



# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data) 
# res = filter(lambda x: x % 2 == 0, res) # выбирает значения х, которые отвечают условию х % 2 == 0
# res = list(map(lambda x: (x, x ** 2), res)) # [(2, 4), (8, 64), (38, 1444)]
# print(res)


my_list = list(map(int, list('1234567890')))
print (my_list)

def even (num: int):
    if num % 2 == 0:
        return True
    return False

even_list = list(filter(even, my_list))
print(even_list)