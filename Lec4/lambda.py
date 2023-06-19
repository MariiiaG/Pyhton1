# Урок 4. Функции высшего порядка, работа с файлами

# Анонимные, lambda-функции

# def f(x):
#     return x * x

# a = f # переменная, которая хранит в себе ссылку на функцию f
# print(type(a)) # <class 'function'>
# print(f(5)) # 25
# print(a(5)) # 25


# # def calc1(a, b):
# #     return a + b

# def calc2(a, b):
#     return a * b

# def math(op, x, y): # op - функция и переменные x, y
#     print(op(x, y))
    
# calc1 = lambda a,b: a + b #  сработает так же как def calc1 ранее

# math(lambda a, b: a + b, 5, 45) # 50
# math(calc1, 5, 45) # 50
# math(calc2, 5, 45) # 225



# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число, квадрат числа).
# Пример : 1 2 3 5 8 15 23 38
# Получить : [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data :
#     if i % 2 == 0 :
#         res.append((i, i ** 2))
# print(res)


# def select(f, col):
#     return [f(x) for x in col] # will apply function to f to all elements in col list

# def where(f, col):
#     return [x for x in col if f(x)] # вернет только те элементы, которые выполнили условие f(x)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data) 
# print(res) # [1, 2, 3, 5, 8, 15, 23, 38]
# res = where(lambda x: x % 2 == 0, res) # выбирает значения х, которые отвечают условию х % 2 == 0
# print(res) # [2, 8, 38]
# # res = select(lambda x: (x, x ** 2), res)
# # print(res) # [(2, 4), (8, 64), (38, 1444)]

# res = list(select(lambda x: (x, x ** 2), res))
# print(res)


my_list  = '123jhh45hj6h57h5jh2h452k3h4'
new_list = list(filter(lambda x : x.isdigit(), my_list))
print(new_list) # ['1', '2', '3', '4', '5', '6', '5', '7', '5', '2', '4', '5', '2', '3', '4']