#Найдите три ключа с самыми высокими значениями в
#словаре
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
#после чего эти ключи сохраните в какой либо переменной и удалите
#из предыдущего словаря

keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
a = 0
for i in keys:
    a = my_dict.pop(i)
print(my_dict)