import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(password):
    left_word = []
    right_word = []

    for w in password:
        if w == "<":
            if left_word:
                right_word.append(left_word.pop())
        elif w == ">":
            if right_word:
                left_word.append(right_word.pop())
        elif w == "-":
            if left_word:
                left_word.pop()
        else:
            left_word.append(w)
            
    return "".join(left_word + list(reversed(right_word)))
    
def main():
    T = int(input())
    for _ in range(T):
        password = list(input())

        answer = solve(password)
        print(answer)
    
if __name__ == "__main__":
    main()