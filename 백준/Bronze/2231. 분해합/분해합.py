N = int(input())

for i in range(1, N + 1):
    test_sum = i
    for j in range(len(str(i))):
        test_sum += int(str(i)[j])

    if test_sum == N:
        break

if i == N:
    print(0)
else:
    print(i)
