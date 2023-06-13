# Вважно понимать что, сколько аргументов мы передаем, столько и принимаем. 
# Или наоборот, сколько аргументов мы принимаем, столько и передаем.

# Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     print(summa)

# sum_numbers(5) #вызываем функцию. Заданная переменная равна 5


# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa # return завершает выполнение программы. Написанное после него не будет исполнено
#     print('stop') # won't be executed as it is placed after 'return'

# ## print (sum_numbers(5))
# a = sum_numbers(5)
# print(a)


# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
   
# # a = sum_numbers(5) # no value given for variable y, so function will use the default value 'Hello'
# # print(a)

# print(sum_numbers(5, 'Qwerty')) # y value is stated, and will prevail over the default


# Функция, которая будет принимать неизвестное / неограниченное количество аргументов. 
# Например, если вводим набор букв, из которого потом сотавим слово

def sum_str(*args): # * implies that there will be unknown number of variables
    res = '' # created an empty string variable res
    for i in args :
        res += i
    return res

# print(sum_str('M', 'a', 'r', 'i', 'i', 'a')) # Mariia
# print(sum_str('hello ', 'there, ', 'its me !')) # hello there, its me !
# print(sum_str('1', '2', '3')) # 123
# # print(sum_str(1, 2, 3)) # error. Not a string value