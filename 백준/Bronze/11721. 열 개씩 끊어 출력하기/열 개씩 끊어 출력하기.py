sen = input()

for i in range(1, len(sen) + 1):
    print(sen[i - 1], end = "")
    if i % 10 == 0:
        print()
