from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

ops = []
for i in range(4):
    while op[i] != 0:
        op[i] -= 1
        ops.append(i)

max_op = float("-inf")
min_op = float("inf")
for o in set(permutations(ops, len(ops))):
    answer = nums[0]
    for idx, cal in enumerate(o):
        if cal == 0:
            answer += nums[idx + 1]
        elif cal == 1:
            answer -= nums[idx + 1]
        elif cal == 2:
            answer *= nums[idx + 1]
        elif cal == 3:
            answer = int(answer / nums[idx + 1])
    
    if answer > max_op:
        max_op = answer
    if answer < min_op:
        min_op = answer

print(max_op)
print(min_op)