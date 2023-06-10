text_Winny = input('Введите строчку песни: ')
list_1 = list(text_Winny.split())
# print(list_1)

list_2 = []
for i in range(len(list_1)):
    count = 0
    vowels = set('уеыаояию')
    for letter in list_1[i]:
        if letter in vowels:
            count +=1
    list_2.append(count)

flag = True
for i in range(len(list_2)-1):
    if list_2[i] != list_2[i+1]:
        flag = False

if flag == True:
    print('Парам пам-пам')
else:
    print('Пам парам')


# функция, вычисляющая элемент по номеру строки и столбца

def operation_table(num_rows, num_columns):
    mas_1 = [[(i+1)*(j+1) for j in range(num_columns)]for i in range(num_rows)]
    return mas_1
print(operation_table(6,6))


num_rows = int(input('Введите число строк: '))
num_columns = int(input('Введите число колонок: '))
for i in range(1, num_rows + 1):
    for j in range(1, num_columns +1):
        print(i*j, end='\t')
    print()
