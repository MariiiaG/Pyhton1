# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 


def find_rhythm (poem_text: str):
    phrases = poem_text.split()
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    vow_count = []
    for phrase in phrases:
        count = sum(i in vowels for i in phrase.lower())
        vow_count.append(count)
    if len(set(vow_count)) == 1:
        print("Парам пам-пам")
    else :
        print ("Пам парам")
        
poem = str(input("Введите стих Винни тут : "))
print(find_rhythm(poem))