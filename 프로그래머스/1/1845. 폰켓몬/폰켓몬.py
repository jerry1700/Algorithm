from collections import Counter

def solution(nums):
    po = Counter(nums)
    
    if len(po) >= len(nums) / 2:
        return len(nums) / 2
    else:
        return len(po)