x = 0
n = int(input())

for i in range(n):
    operationx = input()
    if (
        operationx == "++x"
        or operationx == "x++"
        or operationx == "X++"
        or operationx == "++X"
    ):
        x = x + 1
    elif (
        operationx == "--x"
        or operationx == "x--"
        or operationx == "X--"
        or operationx == "--X"
    ):
        x = x - 1
    else:
        print("BRUH")
print(x)
