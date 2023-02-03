# Задача 2: На столе лежат n монеток. Некоторые
# из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть.

import random

print("Введите количество монет:", end=' ')
n = int(input())
h = int()
ls = list()

count = 0
while count < n:
    h = random.randint(0, 1)
    ls.insert(count, h)
    count += 1
print(f"Раскладка монет: {ls}")
print("где 0 - решка;" + "\n" + "\t" + "1 - орел. ")

N1 = 0
N0 = 0

for i in ls:
    if i == 0:
        N0 += 1
    elif i == 1:
        N1 += 1


if N0>N1:
    print(f"Перевернуть монет: {N1} ")
elif N1>N0:
    print(f"Перевернуть монет: {N0} ")
else:
    print(f"Перевернуть монет: {N0} ")