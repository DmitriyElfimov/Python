# Требуется вычислить сколько раз встречается число Х

import random

n = int(input('Введите число элементов массива: '))
m = int(input('Введите максимальное значение массива: '))

count1 = 0
list_1 = []

for i in range(n):
    a = random.randint(0, m)
    list_1.append(a)

print(list_1)

x = int(input('Введите искомое число массива: '))

for i in range(n):
    if list_1[i] == x:
        count1 += 1

print(f'Число {x} встречается {count1} раз')

# Требуется найти в массиве самый близкий элемент

n = int(input('Введите число элементов массива: '))
m_min = int(input('Введите минимальное значение массива: '))
m_max = int(input('Введите максимальное значение массива: '))

diff = abs(m_max-m_min)
y = 0
list_1 = []

for i in range(n):
    m = random.randint(m_min, m_max)
    list_1.append(m)

print(list_1)

x = int(input('Введите число X: '))

for i in range(n):

    if abs(x - list_1[i]) <= diff:
        diff = abs(x - list_1[i])
        y = list_1[i]

print(f'Самый близкий элемент - это {y}')


# Игра Скрабл

text = input('Введите Ваше слово: ')
summ = 0
n = text.lower()

for i in range(len(n)):
    
    if n[i] == "a":
        summ += 1
    elif n[i] == "e":
        summ +=1
    elif n[i] == "i":
        summ +=1
    elif n[i] == "o":
        summ +=1
    elif n[i] == "u":
        summ +=1
    elif n[i] == "l":
        summ +=1
    elif n[i] == "n":
        summ +=1
    elif n[i] == "s":
        summ +=1
    elif n[i] == "t":
        summ +=1
    elif n[i] == "r":
        summ +=1
    elif n[i] == "d":
        summ +=2
    elif n[i] == "g":
        summ +=2
    elif n[i] == "b":
        summ +=3
    elif n[i] == "c":
        summ +=3
    elif n[i] == "m":
        summ +=3
    elif n[i] == "p":
        summ +=3
    elif n[i] == "f":
        summ +=4
    elif n[i] == "h":
        summ +=4
    elif n[i] == "v":
        summ +=4
    elif n[i] == "w":
        summ +=4
    elif n[i] == "y":
        summ +=4
    elif n[i] == "k":
        summ +=5
    elif n[i] == "j":
        summ +=8
    elif n[i] == "x":
        summ +=8
    elif n[i] == "q":
        summ +=10
    elif n[i] == "z":
        summ +=10
    

    elif n[i] == "а":
        summ += 1
    elif n[i] == "в":
        summ +=1
    elif n[i] == "е":
        summ +=1
    elif n[i] == "и":
        summ +=1
    elif n[i] == "н":
        summ +=1
    elif n[i] == "о":
        summ +=1
    elif n[i] == "р":
        summ +=1
    elif n[i] == "с":
        summ +=1
    elif n[i] == "т":
        summ +=1
    elif n[i] == "д":
        summ +=2
    elif n[i] == "к":
        summ +=2
    elif n[i] == "л":
        summ +=2
    elif n[i] == "м":
        summ +=2
    elif n[i] == "п":
        summ +=2
    elif n[i] == "у":
        summ +=2
    elif n[i] == "б":
        summ +=3
    elif n[i] == "г":
        summ +=3
    elif n[i] == "ё":
        summ +=3
    elif n[i] == "ь":
        summ +=3
    elif n[i] == "я":
        summ +=3
    elif n[i] == "й":
        summ +=4
    elif n[i] == "ы":
        summ +=4
    elif n[i] == "ж":
        summ +=5
    elif n[i] == "з":
        summ +=5
    elif n[i] == "х":
        summ +=5
    elif n[i] == "ц":
        summ +=5
    elif n[i] == "ч":
        summ +=5
    elif n[i] == "ш":
        summ +=8
    elif n[i] == "э":
        summ +=8
    elif n[i] == "ю":
        summ +=8    
    elif n[i] == "ф":
        summ +=10
    elif n[i] == "щ":
        summ +=10
    elif n[i] == "ъ":
        summ +=10

print(f'Стоимость введенного слова = {summ}.')
