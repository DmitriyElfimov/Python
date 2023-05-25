# Определить минимальное число монеток, которое нужно перевернуть, чтобы все были одинаково

import random

n = int(input('Введите число: '))

count1 = 0
count2 = 0
list_1 = []

for i in range(0,n):
    m = random.randint(0, 1)
    list_1.append(m)
    if m == 0:
        count1 += 1
    else:
        count2 += 1
    
print(list_1)

print(f'{count1} монеток лежат вверх решкой, {count2} монеток лежат вверх гербом')

if count1 <= count2:
    print(f'нужно перевернуть решки - {count1} монеток')
else:
    print(f'нужно перевернуть гербы - {count2} монеток')


# Отгадать задуманные числа

n = int(input('Введите сумму чисел X и Y: '))
m = int(input('Введите произведение чисел X и Y: '))

for x in range(1000):
    for y in range(1000):
        if x+y==n and x*y==m:
            print(f'X = {x}; Y = {y}')


# Вывести все степени числа 2 до N

n = int(input('Введите число N: '))

list_1 = []
for i in range(0, n):
    if 2**i < n:
        list_1.append(2**i)

print(list_1)
