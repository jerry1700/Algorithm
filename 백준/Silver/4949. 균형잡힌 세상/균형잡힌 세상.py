import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(test):
    stack = []

    for text in test:
        if text == "(":
            stack.append(text)
        elif text == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(text)
            else:
                return "no"
        elif text == "[":
            stack.append(text)
        elif text == "]":
            if stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(text)
            else:
                return "no"
    
    if stack:
        return "no"
    else:
        return "yes"

def main():
    while True:
        test = list(input())
        if test == ["."]:
            break

        answer = solve(test)
        print(answer)

if __name__ == "__main__":
    main()