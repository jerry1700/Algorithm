S = input()
asc = [-1] * 128

for i in S:
    if asc[ord(i)] < 1:
        asc[ord(i)] = S.index(i)

print(*asc[97:123])
