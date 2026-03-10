num = [int(input()) for i in range(10)]
remainders = []

for i in num:
    remainders.append(i % 42)

remainders = set(remainders)
print(len(remainders))
