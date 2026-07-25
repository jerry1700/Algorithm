def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        count = (d ** 2 - i ** 2) ** 0.5
        answer += count // k + 1
                
    return answer