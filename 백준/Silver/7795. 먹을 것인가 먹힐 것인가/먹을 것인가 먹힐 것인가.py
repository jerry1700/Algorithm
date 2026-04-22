import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    cnt = 0
    idx = 0

    for a in A:
        while idx < M and a > B[idx]:
            idx += 1
        cnt += idx

    print(cnt)