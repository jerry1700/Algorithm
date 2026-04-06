N = int(input())
members = [list(input().split()) for _ in range(N)]

members.sort(key = lambda x: int(x[0]))

for age, name in members:
    print(age, name)