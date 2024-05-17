rounds = int(input())
Mishka = 0
Chris = 0

for i in range(rounds):
    m, c = map(int, input().split())
    if m > c:
        Mishka = Mishka + 1
    elif c > m:
        Chris = Chris + 1

if Mishka > Chris:
    print("Mishka")
elif Mishka == Chris:
    print("Friendship is magic!^^")
else:
    print("Chris")
