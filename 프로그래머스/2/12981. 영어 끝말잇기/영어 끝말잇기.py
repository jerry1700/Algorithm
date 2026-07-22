def solution(n, words):
    wrong = False
    end = words[0][-1]
    for i, word in enumerate(words):
        if i == 0:
            continue
        
        start = word[0]
        if end != start:
            wrong = True
            break
            
        end = word[-1]
    
    overlap = False
    forward = [words[0]]
    for j, word in enumerate(words):
        if j == 0:
            continue
            
        if word in forward:
            overlap = True
            break
            
        forward.append(word)
            
    if not wrong and not overlap:
        answer = [0, 0]
    elif wrong and not overlap:
        if (i + 1) % n == 0:
            x = n
        else:
            x = (i + 1) % n
        if (i + 1) % n == 0:
            y = (i + 1) // n
        else:
            y = (i + 1) // n + 1
        answer = [x, y]
    elif not wrong and overlap:
        if (j + 1) % n == 0:
            x = n
        else:
            x = (j + 1) % n
        if (j + 1) % n == 0:
            y = (j + 1) // n
        else:
            y = (j + 1) // n + 1
        answer = [x, y]
    elif wrong and overlap:
        num = j if i > j else i
        if (num + 1) % n == 0:
            x = n
        else:
            x = (num + 1) % n
        if (num + 1) % n == 0:
            y = (num + 1) // n
        else:
            y = (num + 1) // n + 1
        answer = [x, y]

    return answer