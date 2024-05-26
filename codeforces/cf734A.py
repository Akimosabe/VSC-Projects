n = int(input())
s = str(input())
if s.count("D") > s.count("A"):
    print("Danik")
elif s.count("A") > s.count("D"):
    print("Anton")
else:
    print("Friendship")
