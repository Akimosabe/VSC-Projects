inp = int(input())

for i in range(inp):
    n = list(map(int, input().split()))
    if n[0] < n[1] < n[2]:
        print("STAIR")
    elif n[0] < n[1] > n[2]:
        print("PEAK")
    else:
        print("NONE")
