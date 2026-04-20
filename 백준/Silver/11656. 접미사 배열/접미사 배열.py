S = input()

suffix = [S[i:] for i in range(len(S))]

print(*sorted(suffix), sep = "\n")