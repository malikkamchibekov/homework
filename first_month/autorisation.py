# Ввести логин и пароль и сравнить. Вывести результат авторизации: True или False

login = input("Введите логин: ")
password = input("Введите пароль ")
login_1 = input("Подтвердите логин: ")
password_1 = input("Подтвердите пароль: ")
if login == login_1 and password == password_1: 
	print("Вход выполнен!")
else: 
	print("Неверное имя пользователя или пароль")
