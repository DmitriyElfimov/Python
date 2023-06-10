# даны два неупорядоченных массива (введены вручную)
# вывести без повтора в порядке возростания все числа, которые общие

n = int(input('Введите число элементов первого массива: '))

m = int(input('Введите число элементов второго массива: '))

list_1 = []
list_2 = []

for i in range(n):
    x = int(input('Введите элемент первого массива: '))
    list_1.append(x)

for i in range(m):
    x = int(input('Введите элемент второго массива: '))
    list_2.append(x)

print(list_1)
print(list_2)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greator = [i for i in array[1:] if i> pivot]
    return quicksort(less) + [pivot] + quicksort(greator)

#print(quicksort(list_1))
#print(quicksort(list_2))

#list_1 = quicksort(list_1)
#list_2 = quicksort(list_2)

list_3 = list(set(list_1).intersection(set(list_2)))

print(quicksort(list_3))



# Нахождение максимального числа ягод

n = int(input('Введите число кустов: '))

list_1 = []

for i in range(n):
    x = int(input(f'Введите число ягод {i+1} куста: '))
    list_1.append(x)

print(list_1)

max_summa = list_1[-1]+list_1[0]+list_1[1]

for i in range(1,n-1):
    if list_1[i-1]+ list_1[i]+list_1[i+1] > max_summa:
        max_summa = list_1[i-1]+ list_1[i]+list_1[i+1]

print(max_summa)