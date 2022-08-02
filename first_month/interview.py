"""Должен
знать либо python, либо java, либо javascript. Возраст от 18 до 65. Опыт
от 3х лет. Зарплата до 60000. Вывести результат, подходит кандидат или
нет.

Язык программирования:
Возраст:
Опыт:
Желаемая зарплата:"""

language = input("Введите язык программирования: ")
age = int(input("Введите возраст кандидата: "))
experience = int(input("Введите опыт кандидата: "))
salary = int(input("Введите желаюмую зарплату кандидата: "))
if language == "python" or language == "java" or language == "javascrpit": 
	if age >= 18 and age <= 65 and experience >= 3 and salary <= 60000:
		print ("Этот кандидат подходит!")
	else:
		print ("Этот кандидат НЕ подходит!")
else:
	print ("Этот кандидат НЕ подходит!")
