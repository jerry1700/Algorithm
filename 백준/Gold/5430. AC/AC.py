import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solve(p, nums):
    deq = deque(nums.split(",")) if nums else deque()
    reverse_flag = False

    for order in p:
        if order == "R":
            reverse_flag = not reverse_flag
        elif order == "D":
            if not deq:
                return "error"
            if reverse_flag:
                deq.pop()
            else:
                deq.popleft()
        
    if reverse_flag:
        deq.reverse()
    
    return "[" + ",".join(deq) + "]"

def main():
    T = int(input())

    for _ in range(T):
        p = input()
        n = int(input())
        nums = input()[1:-1]

        answer = solve(p, nums)
        print(answer)

if __name__ == "__main__":
    main()