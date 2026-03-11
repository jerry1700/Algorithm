L, C = map(int, input().split())
word = sorted(list(input().split()))

vowel = "aeiou"

def backtracking(start, depth):
    vowel_cnt = 0
    if depth == L:
        for v in vowel:
            if v in password:
                vowel_cnt += 1
        consonant_cnt = L - vowel_cnt
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print("".join(password))
        return
    
    for i in range(start, C):
        password.append(word[i])
        backtracking(i + 1, depth + 1)
        password.pop()

password = []
backtracking(0, 0)