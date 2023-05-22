# Задача 1 : За день машина проезжает n км. Сколько дней нужно, чтобы проехать маршрут длиной m км ?
# При решении нельзя пользоваться условной конструкцией if и циклами
# n = 700 ; m = 750

# print ("Enter distance in kilometers : ")
# dist = int(input ())

# print ("Enter kilometers you can cover in a day : ")
# speed = int(input ())

# days = dist // speed + (dist % speed > 0)  # bool. True = 1
# print (days)
# # print (f"You will need {dist // speed + (dist % speed > 0)} day(s)")

# Задача 2 : В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты 
# для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся 
# в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:** 1) 20, 2) 21, 3) 22
# **Output:**
# 32

# print ("How many students are there in Class A : ")
# a = int(input())
# print ("How many students are there in Class B : ")
# b = int(input())
# print ("How many students are there in Class C : ")
# c = int(input())    
# # # tables = a//2 + (a%2 > 0) + b//2 + (b%2 > 0) + c//2 + (c%2 > 0)
# # # print(tables)
# # print(f"You'll need to get {a//2 + (a%2 > 0) + b//2 + (b%2 > 0) + c//2 + (c%2 > 0)} tables")

# # another option :
# tables = (a +1) // 2 + (b +1) // 2 + (c +1) // 2 # by adding 1 to each group we ensure theres enough tables
# print(tables)                                    # for classes with odd number of students

# Задача 3 : Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать 
# или сообщать, что без дополнительной информации это сделать невозможно.
# **Input:**
# 3
# 4
# **Output:**
# 6

# print ("How many cars did you pass by ? : ")
# i = int(input ())
# print ("What's the number of your car ? : ")
# j = int(input ())
# if i == j :
#     print ("Not enough info :(")
# else :
#     print (f"There's {i + j - 1} cars in this train")

# Задача 4 : Дано натуральное число. Требуется определить, является ли год с данным номером високосным
# Если год является високосным, то выведите YES, иначе выведите NO.
# Год является високосным, если его номер кратен 4, но не крвтен 100, а также, если он кратен 400
# Ex.: 2016 YES !

# print ("Enter year : ")
# year = int (input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
#     print("YES !")
# else :
#     print ("NO :(")