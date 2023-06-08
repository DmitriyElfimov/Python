# Заполнение массива элементами ариметической прогрессии

a1 = int(input('Введите первый элемент: '))
differ = int(input('Введите разность: '))
amount = int(input('Введите колличество элементов: '))
list_1 = []

list_1 = list(map(lambda x: a1 + x * differ, range(amount)))

print(list_1)


# Определить индексы элементов, удовлетворяющих требованию

list_1 = []
list_1 = list(map(int, input('Введите элементы массива: ').split()))
print(list_1)

mini_m = int(input('Введите минимальное значение диапазона: '))
maxi_m = int(input('Введите максимальное значение диапазона: '))

list_index_total = []
for x in range(len(list_1)):
    if mini_m < list_1[x] < maxi_m:
        list_index_total.append(x)

print(list_index_total)