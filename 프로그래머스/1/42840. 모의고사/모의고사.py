def solution(answers):
    result = [0, 0, 0]
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i, answer in enumerate(answers):
        if answer == one[i]:
            result[0] += 1
        if answer == two[i]:
            result[1] += 1
        if answer == three[i]:
            result[2] += 1
    
    students = []
    p = max(result)
    for i, r in enumerate(result):
        if r == p:
            students.append(i + 1)
            
    return students