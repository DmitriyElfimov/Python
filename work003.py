# сколько раз встречается каждая буква

str_1 = input('Введите сроку: ')
start = -1

count_a = 0
count_b = 0
count_c = 0
count_d = 0
while True:
    start = str_1.find('a', start+1)
    if start == -1:
        break
    count_a += 1
while True:
    start = str_1.find('b', start+1)
    if start == -1:
        break
    count_b += 1
while True:
    start = str_1.find('c', start+1)
    if start == -1:
        break
    count_c += 1
while True:
    start = str_1.find('d', start+1)
    if start == -1:
        break
    count_d += 1
print(f'a_{count_a}, b_{count_b}, c_{count_c}, d_{count_d}')


# бинарный поиск элемента

array = [1,2,3,4,5,6,7,8,9,10]
x = int(input('Введите число: '))

left = 0
right = len(array) - 1
middle = len(array)//2

while x != array[middle]:
    if x < array[middle]:
        right = middle -1
    else: left = middle + 1
    middle = (left + right) // 2
    if left >= right:
        break

if x == array[middle]:
    print(f'Индекс элемента = {middle}')
else:
    print('Такого элемента нет')



# последовательность фибонначи

def fibo (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibo(n-1) + fibo(n-2)

n = int(input('Введите число: '))

print(fibo(n))


# Хакер Василий


array = [1,3,3,3,4]
min_m = max_m = array[0]

for i in range(1, len(array)):
    if array[i] < min_m:
        min_m = array[i]
    if array[i] > max_m:
        max_m = array[i]

for i in range(len(array)):
    if array[i] == max_m:
        array[i] = min_m

print(array)

# Проверка простое число или нет

import math

n = int(input('Введите Ваше число: '))
flag = True
i = 2

while i <= math.sqrt(n):
    if n % i == 0:
        flag = False
        break
    i += 1

if flag:
    print('число простое')
else:
    print('число составное')

