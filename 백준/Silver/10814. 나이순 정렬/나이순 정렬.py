N = int(input())

age_name = [input().split() for i in range(N)]
sort_age_name = sorted(age_name, key = lambda x: int(x[0]))

for age, name in sort_age_name:
    print(age, name)
