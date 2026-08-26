from itertools import product

def solution(word):
    vowel = ["A", "E", "I", "O", "U"]
    dic = []
    
    for i in range(1, 6):
        dic.extend(''.join(p) for p in product(vowel, repeat=i))
        
    dic.sort()
    
    return dic.index(word) + 1