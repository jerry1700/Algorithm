N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def move_dice(oper):
    if oper == 1:
        dice[0], dice[1], dice[2], dice[5] = dice[2], dice[0], dice[5], dice[1]
    elif oper == 2:
        dice[0], dice[1], dice[2], dice[5] = dice[1], dice[5], dice[0], dice[2]
    elif oper == 3:
        dice[0], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[3]
    elif oper == 4:
        dice[0], dice[3], dice[4], dice[5] = dice[3], dice[5], dice[0], dice[4]

for op in order:
    if not (0 <= x + dxy[op - 1][0] < N and 0 <= y + dxy[op - 1][1] < M):
        continue

    x, y = x + dxy[op - 1][0], y + dxy[op - 1][1]
    move_dice(op)

    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    if dice[0] != 0:
        print(dice[0])
    else:
        print(0)