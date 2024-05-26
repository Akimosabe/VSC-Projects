n = int(input())
x = 0

for i in range(n):
    p, q = map(int, input().split())
    # p - количество людей которые уже живут в команте, q - допустимое количество жильцов
    if p + 2 <= q:
        x = x + 1
print(x)
