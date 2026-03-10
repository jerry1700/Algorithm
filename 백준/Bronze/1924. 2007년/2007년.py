x, y = map(int, list(input().split(" ")))

if x == 1:
    day = y
elif x == 2:
    day = 31 + y
elif x == 3:
    day = 31 + 28 + y
elif x == 4:
    day = 31 + 28 + 31 + y
elif x == 5:
    day = 31 + 28 + 31 + 30 + y
elif x == 6:
    day = 31 + 28 + 31 + 30 + 31 + y
elif x == 7:
    day = 31 + 28 + 31 + 30 + 31 + 30 + y
elif x == 8:
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + y
elif x == 9:
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + y
elif x == 10:
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + y
elif x == 11:
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + y
elif x == 12:
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + y

if day % 7 == 0:
    print("SUN")
elif day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
else:
    print("SAT")
