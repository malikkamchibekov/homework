# Напишите программу, которая рассчитает сколько бензина израсходовал транспорт в ср. на 100 км.

fuel = float(input("Введите кол-во литров израсходованных за дорогу: "))
s = float(input("Введите пройденное расстояние в км: "))
average = fuel / s * 100 
print ("средний расход топлива л/100 км: ", average)
