# Функция map
# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта 
# и возвращает итератор с новыми объектами.

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x : x + 10, list_1))
# print(list_1)


# data = '12 4 656 334 75 2 65 2 47'
# print(data) #  string value 12 4 656 334 75 2 65 2 47
# print(type(data))
# data = data.split()
# print(data) # list of string values  ['12', '4', '656', '334', '75', '2', '65', '2', '47']
# print(type(data))


# data = '12 4 656 334 75 2 65 2 47'
# data = list(map(int, data.split()))
# print(data) # list of integers [12, 4, 656, 334, 75, 2, 65, 2, 47]


# def where(f, col):
#     return [x for x in col if f(x)] # вернет только те элементы, которые выполнили условие f(x)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data) 
# print(res) # [1, 2, 3, 5, 8, 15, 23, 38]
# res = where(lambda x: x % 2 == 0, res) # выбирает значения х, которые отвечают условию х % 2 == 0
# print(res) # [2, 8, 38]
# res = list(map(lambda x: (x, x ** 2), res)) # [(2, 4), (8, 64), (38, 1444)]
# print(res)



# my_list = list('123456789')
# print(my_list)

# # for i in range (len(my_list)):
# #     my_list[i] = int(my_list[i])

# my_list = list(map(int, my_list))  # same as ^ but using map
# print(my_list)