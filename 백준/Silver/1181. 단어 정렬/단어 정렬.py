import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
words = list(set(input() for _ in range(N)))

words = sorted(words, key = lambda x: (len(x), x))

print(*words, sep = "\n")