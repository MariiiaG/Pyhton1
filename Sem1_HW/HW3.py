# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

print("Введите номер вашего билета : ")
num = int(input())
last = 0
first = 0

while num >= 1000 :
    x = num % 10
    last += x
    num //= 10

else: 
    while num > 0 :
     y = num % 10
     first += y
     num //= 10

if first == last :
   print ("YES ! :D")
else :
   print ("NO")
