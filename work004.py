import random

print(my_list := [random.randint(0,100) for _ in range(10)])

for i in range(100):
    print(my_list[i%len(my_list)])


list_size = int(input('Введите количество элементов списка: '))
print(list_1 := [random.randint(0,10) for i in range(list_size)])
set_1 = set(list_1)
count = 0
for i in set_1:
    count += list_1.count(i) // 2

print(f'Количество пар в списке: {count}')


# Дружественные числа

def sum_div(n):
    sum_1 = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum_1 += i
    return sum_1

empty_dictionary = {}
k = 10000

list_1 = []
for i in range(1,k+1):
    empty_dictionary[i] = sum_div(i)

for j in empty_dictionary:
    if j == empty_dictionary.get(empty_dictionary.get(j)) and j < empty_dictionary.get(j):
        print(j,empty_dictionary.get(j))


#orbits = [(1,3), (2.5,10), (7,2), (6,6), (4,3)]

#def find_farthest_orbit():


#print(find_farthest_orbit(orbits))

