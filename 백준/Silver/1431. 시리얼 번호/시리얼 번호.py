N = int(input())
guitars = [input() for _ in range(N)]

guitars.sort(key = lambda x: (len(x), sum(int(i) for i in x if i.isdigit()), x))

print(*guitars, sep = "\n")