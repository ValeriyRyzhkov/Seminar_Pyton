# Программа принимает на вход 5 числе и находит максимальное из них

# ВАРИАНТ 1
# numbers = []
# for i in range(5):
#     n = int(input('Введите число: '))
#     numbers.append(n)
# print(numbers)
# maxx = numbers[0]
# for i in numbers:
#     if i > maxx:4
# maxx = i
# print(maxx)

# ВАРИАНТ 2
#numbers = []
#for _ in range(5):
#    n = int(input('Введите число: '))
#    numbers.append(n)
#print(numbers)        # вывод списка, если нужно
#print(max(numbers))   #это готовая функция поиска максимального числа

# ВАРИАНТ 3

maxx = int(input('Введите первое число: '))
for _ in range(4):
    n = int(input('Введите число: '))
    if n > maxx:
        maxx = n
print(maxx)   #это готовая функция поиска максимального числа