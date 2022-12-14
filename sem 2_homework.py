# ДОМАШНЕЕ ЗАДАНИЕ

# 14. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#N = input('Введите число N = ')
#summa = 0
#for i in N:
#    if i.isalnum():   #метод проверки, состоит ли строка из цифр или букв. Еще можно метод S.isdigit()
#        summa += int(i)   #ставить только "=", то программа возьмет только последнее число
#print(summa)

# 15. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#N = int(input('Введите число N больше единицы = '))
#rezult = 1
#list = []
#for i in range (1, N+1):
#    list.append(rezult*i)   # метод s.append добавляет элемент в конец списка
#    rezult *= i
#print(list)

# 16. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# последовательность по-человечески:(1 + 1/n)**n

#n = int(input('Введите число N больше единицы = '))
#rezult = 0
# for i in range (1, n+1):
#    rezult += ((1 + 1/n)**n) 
#print(rezult)

# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# 18. Реализуйте алгоритм перемешивания списка.

from random import *
N = [1, 2, 3, 4, 5, 6]
shuffle(N)   #функция перемешивания списка
print(N)