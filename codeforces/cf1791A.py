a, b = map(int, input().split())
b = int(input())
y = 0
while a <= b:
    a = a * 3
    b = b * 2
    y = y + 1
print(y)
