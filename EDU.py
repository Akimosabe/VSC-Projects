import random

numbers = [4, 8, 15, 16, 23, 42]
count = [0] * len(numbers)

for i in range(len(numbers)):
    while True:
        num = random.randint(1, 50)
        count[i] += 1
        if num == numbers[i]:
            print(num, end=" ")
            break
print()
print('Количество попыток:', count)
print('Общее количество:', sum(count))
