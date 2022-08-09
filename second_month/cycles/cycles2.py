#Сформировать
#из введенного числа обратное по порядку входящих в него цифр и вывести
#на экран. Например, если введено число 3486, то надо вывести число 6843.
value = int(input("Введите число: "))
reverse_value = 0
while value > 0:
    reverse_value = reverse_value * 10 + value % 10
    value = value // 10
print(reverse_value)

