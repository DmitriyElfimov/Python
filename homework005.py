# Возведение в степень рекурсией

def degree_numbers (x, y):
    
    if y > 0:
        product = x * degree_numbers(x, y-1)
        y -= 1
    elif y == 0: product = 1
    return product


x = int(input('Введите число возводимое в степень: '))
y = int(input('Введите степень: '))

print(degree_numbers(x, y))

# сумма двух чисел рекурсией

def summ_numbers (x, y):
    
    if x > 1:
        summa = 1 + summ_numbers(x-1, y)
        x -= 1
    else: 
        if y > 0:
            summa = 1 + summ_numbers(x, y-1)
            y -= 1
        else: summa = x
    return summa

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

print(summ_numbers(x, y))