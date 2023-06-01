# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. 
# В словаре для определения элемента используется значение ключа (строка, число).

# d = {} # создать пустой словарь
# d = dict() # создать пустой словарь

# d['q'] = 'qwerty' # внесли значение. По ключу 'q' мы получим значение 'qwerty'
# print(d) # {'q': 'qwerty'}
# print(type(d))

# d['w'] = 'werty'
# print(d) # {'q': 'qwerty', 'w': 'werty'}

# print(d['q']) # qwerty

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} 
# print(dictionary['left']) # ←
# print(dictionary['up']) # ↑
# dictionary['left'] = '⇐' # поменяли на другой тип стрелочки
# print(dictionary['left']) # ⇐
# # могут быть разные типы данных
# dictionary[895] = 98998
# print(dictionary) # {'up': '↑', 'left': '⇐', 'down': '↓', 'right': '→', 895: 98998}
# ## print(dictionary['type']) # KeyError: 'type' выдаёт ошибку, тк нет такого ключа
# del dictionary['left'] # удаление элемента
# print(dictionary) # {'up': '↑', 'down': '↓', 'right': '→', 895: 98998}

# for item in dictionary:
#     print(item) # выводит все ключи в столбик 

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item])) # выводит ключи и их значения в столбик
    
# for (k,v) in dictionary.items():
#     print(k, v) # same result as above. Prints keys and its values
    
# print(dictionary.items()) # dict_items([('up', '↑'), ('down', '↓'), ('right', '→'), (895, 98998)])
#         # список из кортежей, составленных из ключей и их значений
