test = list(map(int, input().split()))

if test == sorted(test):
    print("ascending")
elif test == list(reversed(sorted(test))):
    print("descending")
else:
    print("mixed")
