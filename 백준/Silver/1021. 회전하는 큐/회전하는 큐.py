import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solve(N, place):
    start = deque(range(1, N + 1))
    cnt = 0

    for i in place:
        while True:
            if i == start[0]:
                start.popleft()
                break
            elif len(start) - start.index(i) - 1 >= start.index(i):
                start.append(start.popleft())
                cnt += 1
            else:
                start.appendleft(start.pop())
                cnt += 1

    return cnt

def main():
    N, M = map(int, input().split())
    place = list(map(int, input().split()))

    answer = solve(N, place)
    print(answer)

if __name__ == "__main__":
    main()