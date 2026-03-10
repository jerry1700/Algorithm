import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
cnt = [0] * 10001 

for i in range(N):
    cnt[int(input())] += 1

for i in range(10001):
    if cnt[i] != 0:
        result = str(i) + "\n"
        for j in range(cnt[i]):
            print(result)
