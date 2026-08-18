def solution(array, commands):
    answer = []
    for group in commands:
        nums = sorted(array[group[0] - 1:group[1]])
        answer.append(nums[group[2] - 1])
        
    return answer