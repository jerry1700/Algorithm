T = int(input())

for test in range(1, T + 1):
    H, W, N = map(int, input().split())

    if N % H == 0:
        floor = H
        room_no = N // H
    else:
        floor = N % H
        room_no = N // H + 1

    if room_no < 10:
        print(str(floor) + "0" + str(room_no))
    else:
        print(str(floor) + str(room_no))
