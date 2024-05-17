n, k = map(int, input().split())

an = list(map(int, input().split()[:n]))

# n - общее число участников
# чтобы пройти нужно занять k+1

approve = 0

for i in range(n):
    if an[k - 1] == 0 and an[k - 1] == an[i]:
        approve = approve + 0
    elif an[k - 1] <= an[i]:
        approve = approve + 1

print(approve)
