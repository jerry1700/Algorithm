def solution(n, words):
    wrong = False
    end = words[0][-1]
    forward = [words[0]]
    for i, word in enumerate(words):
        if i == 0:
            continue
        
        start = word[0]
        if end != start:
            wrong = True
            break
        end = word[-1]

        if word in forward:
            wrong = True
            break
        forward.append(word)
            
    if wrong:
        if (i + 1) % n == 0:
            x = n
        else:
            x = (i + 1) % n
        if (i + 1) % n == 0:
            y = (i + 1) // n
        else:
            y = (i + 1) // n + 1
        answer = [x, y]
    else:
        answer = [0, 0]

    return answer