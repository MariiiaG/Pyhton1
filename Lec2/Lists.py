# Урок 2. Коллекции данных. Профилирование и отладка

# list_1 = [] # Создание пустого списка 
# list_2 = list() # Создание пустого списка 
# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1) # печатает содержимое списка в квадратных скобках
# print(*list_1) # печатает содержимое списка без скобок

# for i in list_1 : #поочерёдно выведет элементы списка
#     print(i)

# В списках существует нумерация, которая начинается с 0, чтобы вывести первый элемент списка 
# воспользуемся следующей конструкцией:

# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[0]) # 7
# print(list_1[4]) # 15
# print(list_1[-1]) # 17 последний элемент списка

# # Чтобы узнать количество элементов в списке необходимо использовать функцию len(имя_списка)

# list_1 = [7, 9, 11, 13, 15, 17]
# print(len(list_1)) # 6

# Можно список заполнять не только при его создание, но и во время работы программы:

# list_2 = [1, 5]
# print(list_2)
# list_2.append(8) # добавит элемент в конец списка [1, 5, 8]
# print(list_2)
# list_2.append(54) # [1, 5, 8, 54]
# print(list_2)

# list_2 = list() # создание пустого списка 
# for i in range(5): # цикл выполнится 5 раз
#     n = int(input()) # пользователь вводит целое число
#     list_2.append(n)
# print(list_2)

# list_1 = []
# print(list_1)
# for i in range(5) : # переберёт значения от 0 до 4
#     list_1.append(i)
#     print(list_1) # после последней итерации результат - [0, 1, 2, 3, 4]

# Удаление последнего элемента списка

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# a = list_1.pop() 
# print(a) # 7

# print(list_1) # [12]
# print(list_1.pop()) # 12
# print(list_1) # []

# Удаление конкретного элемента из списка

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(1)) # 7
# print(list_1) # [12, -1, 21, 0]

# Добавление элемента на нужную позицию

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # вставит число 11 на 2-ю позицию
# print(list_1)

# Срез списка

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) #10
# print(list_1[-5]) # 6
# print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3,4,5,6,7,8,9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) #[1,7] с 0 до последней позиции с шагом 6
# print(list_1[::6]) # [1, 7] ^ same
   