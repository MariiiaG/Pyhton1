# Напищите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n

# import random

# my_list = [random.randint(0, 10) for _ in range(20)]
# print(my_list)

# counter = {}

# for items in my_list :
#     counter[items] = counter.get(items, 0) + 1
#     if counter.get(items) < 2 :
#         print(items, end=' ')
#     else :
#         print(str(items) + '_' + str(counter.get(items) - 1), end=' ')
        
        
# my_dict = {1: 'one', 2: 'two'}

# print(my_dict[1]) #'one'
# # print(my_dict[3]) # error
# print(my_dict.get(1, 0)) # looks for an item with index 1, if item not found, prints given value - zero
# print(my_dict.get(3, 'ooops')) # no item with index 3, so it will print 'ooops' instead


# Пользователь вводит текст (строка). Словом считается последовательность непробельных символов идущих подряд. 
# Слова разделены одним или большим количеством пробелов или символами конца строки. 
# Опредлелите, сколько различных слов содержится в тексте

# text = """She sells sea shells on the sea shore 
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"""
# unique = set(text.lower().split())
# print(unique)

# print(len(set(text.lower().split()))) #14 because it counts 'sure' and 'sure.' as two unique words

# Better option :
    
# from string import punctuation
# text = """She sells sea shells on the sea shore 
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"""

# for ch in punctuation:
#     text = text.replace(ch, '')
    
# text = text.lower().split()
# print(text)
# print(len(set(text)))
