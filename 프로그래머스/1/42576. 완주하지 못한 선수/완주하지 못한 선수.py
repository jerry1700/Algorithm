def solution(participant, completion):
    people = {}
    for p in participant:
        if p in people:
            people[p] += 1
        else:
            people[p] = 1
            
    for c in completion:
        people[c] -= 1
        
    return next((k for k, v in people.items() if v == 1))