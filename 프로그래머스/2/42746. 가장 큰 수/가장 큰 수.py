def solution(numbers):
    numbers = sorted([str(i) for i in numbers], key=lambda x: x * 3, reverse=True)
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
        
    return answer