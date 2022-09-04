# Программа принимает на вход число N и выводитна экран числа от -N до N с шагом 1
print('Введите число N: ');
N = int (input())
for i in range (-N, N):
    print(i, end=', ' )
print(N)
