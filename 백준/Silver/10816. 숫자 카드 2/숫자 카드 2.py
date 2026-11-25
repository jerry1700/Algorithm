N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
answer_list = list(map(int, input().split()))

group = [0] * 20000001

for num in num_list:
    group[num - 10000000] += 1

for p in answer_list:
    print(group[p - 10000000], end = " ")