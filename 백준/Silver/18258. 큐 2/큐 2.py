import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N):
    q = []
    output = []
    head = 0

    for _ in range(N):
        order = input().split()
        op = order[0]

        if op == "push":
            q.append(order[1])
        elif op == "pop":
            if head < len(q):
                output.append(q[head])
                head += 1
            else:
                output.append(-1)
        elif op == "size":
            output.append(len(q) - head)
        elif op == "empty":
            if head < len(q):
                output.append(0)
            else:
                output.append(1)
        elif op == "front":
            if head < len(q):
                output.append(q[head])
            else:
                output.append(-1)
        else:
            if head < len(q):
                output.append(q[-1])
            else:
                output.append(-1)
    
    return output

def main():
    N = int(input())
    
    answer = solve(N)
    sys.stdout.write("\n".join(map(str, answer)) + "\n")

if __name__ == "__main__":
    main()