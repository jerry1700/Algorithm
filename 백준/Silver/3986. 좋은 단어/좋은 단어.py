import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(words):
    cnt = 0

    for word in words:
        stack = []

        for w in word:
            if stack and stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
        
        if not stack:
            cnt += 1

    return cnt

def main():
    N = int(input())
    words = [input() for _ in range(N)]

    answer = solve(words)
    print(answer)

if __name__ == "__main__":
    main()