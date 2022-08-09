#Написать программу калькулятор оценок. Даны списки оценок с
#предметами трех студентов. В каждом списке содержиться 7
#предметов с оценками, необходимо сконвертировать в словарь и
#найти средний балл оценок данных студентов. И выбрать лучшего
#студента в группе.
#Например:
#ввод данных
#John = [[algebra“, 100], [„biologia“, 84], [„fizika“: 61]]
#вывод: оценки
#John   : {'algebra': 100, 'biologia': 84, 'fizika': 61}
#Средний балл
#John   : 81 балл
#Лучшим студентом является: {имя студенто у которго больше всех
#балл}

john = [["algebra", 100], ["biologia", 84], ["fizika", 61], ["history", 76], ["literatura", 88], ["fizra", 99], ["filosofia", 78]]
michael = [["algebra", 86], ["biologia", 64], ["fizika", 91], ["history", 46], ["literatura", 67], ["fizra", 94], ["filosofia", 92]]
jack = [["algebra", 91], ["biologia", 93], ["fizika", 78], ["history", 65], ["literatura", 91], ["fizra", 82], ["filosofia", 72]]
john_dict = dict(john)
michael_dict = dict(michael)
jack_dict = dict(jack)
print(f'''
John - {john_dict}
Jack - {jack_dict}
Michael - {michael_dict}
''')
avg_mark_john = 0
avg_mark_michael = 0
avg_mark_jack = 0
for i in john_dict:
    avg_mark_john += john_dict.get(i)
for i in michael_dict:
    avg_mark_michael += michael_dict.get(i)
for i in jack_dict:
    avg_mark_jack += jack_dict.get(i)
avg_mark_john = int(avg_mark_john / len(john_dict))
avg_mark_michael = int(avg_mark_michael / len(michael_dict))
avg_mark_jack = int(avg_mark_jack / len(jack_dict))
print(f'''
Средний балл Джона - {avg_mark_john}
Средний балл Майкла - {avg_mark_michael}
Средний балл Джэка - {avg_mark_jack}
''')
if avg_mark_john > avg_mark_michael and avg_mark_john > avg_mark_jack:
    print("Лучшим студентом является John!")
elif avg_mark_michael > avg_mark_jack:
    print("Лучшим студентом является Michael!")
else:
    print("Лучшим студентом является Jack!")

