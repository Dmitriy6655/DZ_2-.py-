# Задача 3: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

print("Введите сумму двух чисел: ", end="")
x = int(input())
print("Введите произведение этих же чисел: ", end="")
y = int(input())

for i in range(x):
    for d in range(y):
        if x == i + d and y == i * d:
            print(f"число 1 равно: {i}; число 2 равно: {d}")
