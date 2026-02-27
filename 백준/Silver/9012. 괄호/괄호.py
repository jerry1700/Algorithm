T = int(input())

for test in range(1, T + 1):
    text = input()

    stack = []
    for i in text:
        if i == "(":
            stack.append(i)
        elif stack and i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == ")":
            stack.append(i)

    if stack:
        print("NO")
    else:
        print("YES")
