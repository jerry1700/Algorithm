N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def stair_check():
    global cnt

    for i in range(N):
        diff = []
        used = [False] * N

        for j in range(N - 1):
            if board[i][j] != board[i][j + 1]:
                diff.append((j, j + 1))
        
        pop_idx = []
        for idx, xy in enumerate(diff):
            x, y = xy
            if abs(board[i][x] - board[i][y]) != 1:
                break

            if board[i][x] > board[i][y]:
                if y + L > N:
                    break
                if any(used[y:y + L]):
                    break
                stair = board[i][y:y + L]
                if len(stair) == L and len(set(stair)) == 1:
                    pop_idx.append(idx)
                    used[y:y + L] = [True] * L
            elif board[i][x] < board[i][y]:
                if x - L + 1 < 0:
                    break
                if any(used[x - L + 1:x + 1]):
                    break
                stair = board[i][x - L + 1:x + 1]
                if len(stair) == L and len(set(stair)) == 1:
                    pop_idx.append(idx)
                    used[x - L + 1:x + 1] = [True] * L

        for i in pop_idx[::-1]:
            diff.pop(i)

        if len(diff) == 0:
            cnt += 1

cnt = 0
stair_check()
board = [list(row[::-1]) for row in zip(*board)]
stair_check()

print(cnt)