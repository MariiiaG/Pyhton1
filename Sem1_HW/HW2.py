# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print ("Сколько журавликов ребята сделали вместе : ")
sum = int(input())
K = sum / 3 * 2
PS = sum / 3 / 2

print (f"Катя сделала {int(K)} журавликов, а Петя и Серёжа каждый по {int(PS)}")