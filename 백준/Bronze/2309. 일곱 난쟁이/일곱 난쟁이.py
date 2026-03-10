import sys

def input():
    return sys.stdin.readline()

def solve(heights):
    bye = sum(heights) - 100

    for i in range(9):
        for j in range(i + 1, 9):
            if heights[i] + heights[j] == bye:
                heights.pop(j)
                heights.pop(i)
                return sorted(heights)

def main():
    heights = [int(input()) for i in range(9)]

    answer = solve(heights)
    print(*answer, sep = "\n")
    

if __name__ == "__main__":
    main()