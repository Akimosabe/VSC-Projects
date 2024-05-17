eleph_friend = int(input())

steps = eleph_friend // 5
if eleph_friend % 5 != 0:
    steps = steps + 1
print(steps)
