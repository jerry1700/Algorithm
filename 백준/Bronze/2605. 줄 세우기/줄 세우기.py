n = int(input())
num = list(map(int, input().split()))

students = []
for i in range(n):
    students.insert(i - num[i], i + 1)

print(*students, sep = " ")