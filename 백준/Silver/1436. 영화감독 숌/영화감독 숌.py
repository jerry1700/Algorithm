N = int(input())

num = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                num.append(str(i) + str(j) + str(k) + str(l) + "666")
                num.append(str(i) + str(j) + str(k) + "666" + str(l))
                num.append(str(i) + str(j) + "666" + str(k) + str(l))
                num.append(str(i) + "666" + str(j) + str(k) + str(l))
                num.append("666" + str(i) + str(j) + str(k) + str(l))

title = []
for i in num:
    title.append(int(i))
title = sorted(list(set(title)))

print(title[N - 1])