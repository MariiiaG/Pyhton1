# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

bushes = int(input("Сколько кустов на грядке : "))
target = int(input("У которого куста находится собирающий модуль : ")) - 1 # пользователь вводит числа с 1, не с 0
collect = 0

berries_per_bush = []
for i in range(bushes):
    berries_per_bush.append(randint(1, 100))
print(berries_per_bush)
print(target)

if target == 1 :
    collect = berries_per_bush[target] + berries_per_bush[target+1] + berries_per_bush[-1]
    print(collect)
    
elif target == bushes-1 :
    collect = berries_per_bush[target] + berries_per_bush[0] + berries_per_bush[-2]
    print(collect)

else :
    collect = berries_per_bush[target] + berries_per_bush[target+1] + berries_per_bush[target-1]
    print(collect)

    
