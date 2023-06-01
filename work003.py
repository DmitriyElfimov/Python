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


