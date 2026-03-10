import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for i in range(N)]

num_sum = sum(num)
if num_sum >= 0:
    num_average = int(num_sum / N + 0.5)
else:
    num_average = int(num_sum / N - 0.5)
num_middle = sorted(num)[N // 2]
test = 0
cnt = [0] * 8001
for i in num:
    cnt[i + 4000] += 1
cnt_max = max(cnt)
num_importance = []
for i in range(8001):
    if cnt[i] == cnt_max:
        num_importance.append(i - 4000)

        if len(num_importance) == 2:
            break
num_range = max(num) - min(num)

print(num_average)
print(num_middle)
print(num_importance[-1])
print(num_range)
