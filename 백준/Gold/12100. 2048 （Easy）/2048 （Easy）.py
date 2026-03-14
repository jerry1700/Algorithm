N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def backtracking(depth):
    if depth == 5:
        sequences.append(sequence[:])
        return
    for i in range(4):
        sequence.append(i)
        backtracking(depth + 1)
        sequence.pop()

def left_rotate(test):
    return [list(row) for row in zip(*test)][::-1]
def right_rotate(test):
    return [list(row) for row in zip(*test[::-1])]

def delete_zero(row):
    no_row = [x for x in row if x != 0]
    return no_row + [0] * (len(row) - len(no_row))

def play(row):
    i = 0
    while i < len(row) - 1:
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
            i += 2
        else:
            i += 1
    return row

def process():
    for i in range(N):
        test[i] = delete_zero(test[i])
    for i in range(N):
        test[i] = play(test[i])
    for i in range(N):
        test[i] = delete_zero(test[i])
    return test

sequences = []
sequence = []
backtracking(0)

max_num = 0
for moves in sequences:
    test = [r[:] for r in board]
    for move in moves:
        if move == 0:
            test = left_rotate(test)
            test = process()
            test = right_rotate(test)
        elif move == 1:
            test = left_rotate(test)
            test = left_rotate(test)
            test = process()
            test = right_rotate(test)
            test = right_rotate(test)
        elif move == 2:
            test = right_rotate(test)
            test = process()
            test = left_rotate(test)
        elif move == 3:
            test = process()

    for i in range(N):
        for j in range(N):
            if test[i][j] > max_num:
                max_num = test[i][j]

print(max_num)