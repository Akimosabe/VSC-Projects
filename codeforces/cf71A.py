numberwords = int(input())

for i in range(numberwords):
    word = input()

    if len(word) > 10:
        lattern1 = str(len(word) - 2)
        print(word[0] + lattern1 + word[len(word) - 1])
    else:
        print(word)
