n = int(input('Введите число: '))
count = 1
factor = 1

while count <= n:
    factor = factor * count
    count += 1
    
print(f'факториал числа {n} = {factor}')

n = int(input('Введите число: '))
n0 = 0
n1 = 1
n2 = 0

i = 2

while n2 < n:
    n2 = n1 + n0
    n0 = n1
    n1 = n2
    i += 1

if n2 == n:
    print(i)
else: print ('-1')


# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10

# Output: 2

n = int(input("Введите n = "))
count = 0
max1 = 0
for i in range(n):
    temp = int(input())
    if temp > 0:
        count += 1
        if count > max1:
            max1 = count
    else:
        count = 0

print("count = ", max1)


n = int(input())
kg =  int(input())
max1 = kg
min1 = kg

for i in range(n - 1):
    kg =  int(input())
    if kg < min1:
        min1 = kg
    if kg > max1:
        max1 = kg
print(min1, max1)

