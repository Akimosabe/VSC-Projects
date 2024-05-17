n = int(input())

decide = 0

for i in range(n):
    petya, vasya, tonya = map(int, input().split())
    if (
        petya == 1
        and vasya == 1
        or petya == 1
        and tonya == 1
        or vasya == 1
        and tonya == 1
    ):
        decide = decide + 1
print(decide)
