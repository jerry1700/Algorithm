N = int(input())
guitars = [input() for _ in range(N)]

for i in range(N):
    for j in range(N - 1 - i):
        if len(guitars[j]) > len(guitars[j + 1]):
            guitars[j], guitars[j + 1] = guitars[j + 1], guitars[j]

        elif len(guitars[j]) == len(guitars[j + 1]):
            sum1 = 0
            sum2 = 0
            for x in guitars[j]:
                if x.isdigit():
                    sum1 += int(x)
            for y in guitars[j + 1]:
                if y.isdigit():
                    sum2 += int(y)

            if sum1 > sum2:
                guitars[j], guitars[j + 1] = guitars[j + 1], guitars[j]

            elif sum1 == sum2:
                if guitars[j] > guitars[j + 1]:
                    guitars[j], guitars[j + 1] = guitars[j + 1], guitars[j]

print(*guitars, sep = "\n")