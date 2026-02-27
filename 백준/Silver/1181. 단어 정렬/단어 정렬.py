N = int(input())

words = [input() for i in range(N)]
words = sorted(list(set(words)))
print("\n".join(sorted(words, key=len)))
