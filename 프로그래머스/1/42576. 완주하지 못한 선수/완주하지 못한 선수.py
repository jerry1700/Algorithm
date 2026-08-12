def solution(participant, completion):
    people = {}
    start = 0
        
    for p in participant:
        people[hash(p)] = p
        start += hash(p)
    
    for c in completion:
        start -= hash(c)
        
    return people[start]