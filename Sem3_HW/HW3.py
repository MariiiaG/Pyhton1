# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# *Пример:*

# ноутбук
#     12

# my_dict = {}
# my_dict = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
# my_dict.update(dict.fromkeys(['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 2))
# my_dict.update(dict.fromkeys(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], 3))
# my_dict.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'], 4))
# my_dict.update(dict.fromkeys(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'], 5))
# my_dict.update(dict.fromkeys(['J', 'X', 'Ш', 'Э', 'Ю'], 8))
# my_dict.update(dict.fromkeys(['Q', 'Z', 'Ф', 'Щ', 'Ъ'], 10))

# word = str(input("Введите слово : "))
# word = word.upper()
# word_score = 0

# for i in word :
#     word_score += my_dict[i]
# print(word_score)



# Решение с семинара : 

letters = {'AEIOULNSTRАВЕИНОРСТ' : 1,
           'DGДКЛМПУ' : 2,
           'BCMPБГЁЬЯ' : 3,
           'FHVWYЙЫ' : 4,
           'KЖЗХЦЧ' : 5,
           'JXШЭЮ' : 8,
           'QZФЩЪ' : 10}

word = input ("Enter the word : ")

total = 0
for ch in word.upper():
    for letter , score in letters.items():
        if ch in letter :
            total += score
            
print(f'Слово "{word}" весит {total} очков')