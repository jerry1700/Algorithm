from collections import Counter

def solution(nums):
    po = Counter(nums)
    
    return min(len(po), len(nums) / 2)