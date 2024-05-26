t = int(input())


for i in range(t):
    n, x = map(int, input().split())
    if n == 1 or n == 2:
        print(1)
    else:
        c = 2
        b = 1
        while n > c:
            c = c + x
            b = b + 1
            # print(c)
        print(b)


# n - номер квартиры
# x - количество квартир на каждом из этажей дома, кроме первого
