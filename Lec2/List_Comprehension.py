# У каждого языка программирования есть свои особенности и преимущества. 
# Одна из культовых фишек Python — list comprehension («генератор списка»). 
# List Comprehension легко читать, и их используют как начинающие, так и опытные разработчики.
# List comprehension — это упрощенный подход к созданию списка, который задействует цикл for, 
# а также инструкции if-else для определения того, что в итоге окажется в финальном списке.

# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.

# list_1 = []
# for i in range(1, 101):
#     list_1.append(i) 
# print(list_1) # [1, 2, 3,..., 100]

# same with list comprehension :
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1)

# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list_1)

# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_3 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),..., (100, 100)]
print(list_3)
list_2 = [(i, i **2) for i in range(1, 101) if i % 2 == 0] # [(2, 4), (4, 16),...., (100, 10000)]
print(list_2)

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_3 = [i * 2 for i in range(10) if i % 2 == 0] 
print(list_3) # [0, 4, 8, 12, 16]