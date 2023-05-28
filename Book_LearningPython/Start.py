# message = "Let's learn Pyhton"
# print (message)

# message = "Changing the message"
# print (message)

# name = "MARIIA gadova"
# print (name.title())  # will capitalize the initials only (result - Mariia Gadova)
# print (name.upper()) # upper case
# print (name.lower()) # lower case

# first_name = "mariia"
# last_name = "gadova"
# full_name = f"{first_name} {last_name}" # f-строки
# print(full_name)
# message = f"Hello, {full_name.title()} !"
# print(message)

# Табуляция
# print ("Python")
# print ("\tPython") # включает отступ в начале строки

# print("Languages: \nPython\nC\nJavaScript") # \n перенос на новую строку

# print("Languages:\n\tPython\n\tC\n\tJavaScript") # \n \t можно комбинировать новая строка + отступ в начале


# Удаление пропусков
favourite_language = "python "
print(favourite_language)
print(favourite_language.rstrip()) # временно удалит лишний пробел у правого края строки

# Чтобы навсегда удалить ненужный пробел надо записать усеченное значение в переменную
favourite_language = favourite_language.rstrip()

favourite_animal = " dog"
print (favourite_animal)
print (favourite_animal.lstrip()) # удаляет лишний пробел слева

favourite_dessert = " ice cream "
print (favourite_dessert)
favourite_dessert = favourite_dessert.strip()
print (favourite_dessert)
