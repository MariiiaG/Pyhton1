# select, then use combination of Command + k then Command + C to comment multiple lines
# to uncomment use Command + k then Command + U
# can also use """ in front and at the end of the block of lines you want to comment
# to run code press Contorl + Fn + F5 
# if you want to introduce a variable, but don't know its value yet use Ex.: n = none

# operators : addition (+), subtraction (-), multiplication (*), division (/), modulus (%), 
# exponentiation (**) возведение в степень, floot division (//) целочисленное деление

# print(5, 7, 8)

# n = 1.87
# print(n)

# n = 'Hello, Mariia' 
# print (n)
# n1 = "Hello again, it's me" # can use either single quotes or double
# print (n1)
# print (type(n1)) # to show data type of the variable
# n2 = '\'Hello' # use \ before a quote mark if you want it to be printed in the result. 
#                 # can also use a mix of ' and " quotes to have string data shown with quotes Ex. : '"Hello"'
# print (n2) 

# a = 5
# b = 1.76
# c = "Hey now"
# print (a, b, c) # to print all 3 variables
# print (a, ' - ', b, ' - ', c) # the variables will be separated by a dash 
# print (f"{a} - {b} - {c}") # same result as the above
# print ("{} - {} - {}".format(a, b, c)) # same as ^

# print ("Enter value for a : ")
# a = input ()
# print (a)

# b = input("Enter value for b :")
# print (b)

# print (a, "+", b, "=", a+b) #doesn't work this way. Will show 2 + 4 = 24

# c = 6.675
# print (c)
# print (type(c))
# c = int(c)
# print (c)
# print (type(c))
# c = str(c)
# print (c + '34')
# print (type(c))
# c = bool(c)
# print(c)
# print (type(c))

# print ("Enter value for a : ")
# a = int(input ())
# print (a)
# b = float(input("Enter value for b :"))
# print (b)
# print (a, "+", b, "=", a+b) # will add the variables as the data types have been indicated

# a = 5.6532465
# b = 3.89347284
# print(round(a*b, 3)) # will multiply a*b and only leave 3 decimal points of the result

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 6 # iter = iter / 6
# iter //= 7 # iter = iter // 7
# iter %= 8 # iter = iter % 8
# iter **= 9 # iter = iter ** 9

# a = 1 > 4
# print (a)
# b = 1 < 4 and 5 > 2
# print (b)
# c = 1 == 2
# print (c)
# d = 1 != 2
# print (d)
# e = 'qwe'
# f = 'qwe'
# print(e == f)
# g = 1 < 3 < 5 < 10 # first compares 1 and 3, then 3 and 5, then 5 and 10
# print (g)

# username = input("Enter your name : ")
# if username == "Mariia":
#     print("Yay ! Hi Mariia !")
# elif username == "Marina":
#     print("I've been waiting for you Marina !")
# elif username == "Ilnar":
#     print("Ilnar, you're the best !!")
# else:
#     print("Hello, ", username, "!")

# n = 423
# sum = 0
# while n > 0:
#     x = n % 10 # остаток от деления на 10 (число 3)
#     sum += x # sum = sum + x
#     n //= 10 # n = n // 10  целочисленное деление на 10 отсекает последнюю цифру
# print (sum)  # finds sum of digits in variable n (4 + 2 + 3 = 9)

# i = 0
# while  i < 5:
#     # if i == 3:
#     #     break   # it is preferably to avoid using breaks. See the next block for an alternative 
#     i += 1
# else:           # will only get to this part if the 'while' condition ends naturally i.e without using 'break'
#     print("Пожалуй")
#     print("хватит )")
# print (i)

# n = int (input()) # программа для нахождения минимального делителя введенного числа
# flag = True
# i = 2
# while flag: # цикл будет выполняться пока flag является true
#     if n % i == 0: # если остаток при делении n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленое на 2
#         print (n)
#         flag = False
#     i += 1

# for i in 1, -2, 3, 14, 6.8:  # переменная i будет поочередно принимать введенные значения
#     print(i)

# r = range (5) # 0, 1, 2, 3, 4
# r = range (2, 5) # 2, 3, 4
# r = range (0, -5) # ----
# r = range (-5, 0) #  -5, -4, -3, -2, -1
# r = range (1, 10, 2) # 1, 3, 5, 7, 9
# r = range (0, 100, -20) # ----

# r = range (100, 0, -20) # 100, 80 60 40 20
# for i in r:
#     print (i)

# for i in range (100, 0, -20): # 100, 80, 60, 40, 20
#     print(i)

# a = 'qwerty'
# print(a[3]) # will only print the 3rd item = letter 'r'
# for i in a:
#     print(i) 

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "+"
#     print(line)

# text = "СъЕШЬ ещё этих МяГкИх французских булочек"
# print(len(text)) #counts the length of the 'text' variable
# print('ещё' in text) # bool. Shows if the given word is found in text
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё', 'ЕЩЁ'))

# text = "СъЕШЬ ещё этих МяГкИх французских булок"
# print(text[0]) # с
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-1]) # к
# print(text[-5]) # б
# print(text[:]) # СъЕШЬ ещё этих МяГкИх французских булок
# print(text[:2]) # Съ shows first two elements
# print(text[len(text)-2:]) # ок
# print(text[20:]) # shows elements starting from the 20th element until the end
# print(text[2:9]) # ЕШЬ ещё
# print(text[6:-18]) # ещё этих МяГкИх
# print(text[0:len(text):6]) # сеикакл startine element : last element : step length
# print(text[::6]) # сеикакл same as ^
# print(text[0:30:5])

# text = "СъЕШЬ ещё этих МяГкИх французских булок"
# text = text[2:9] + text[-5] + text[:2] # (elements from 2 to 8) + (element -5) + (last two) 
# print(text)
