from collections import defaultdict

def dfs(start, tree):
    visited = set([start])
    stack = [start]
    count = 1
    
    while stack:
        x = stack.pop()
        for nx in tree[x]:
            if nx not in visited:
                visited.add(nx)
                stack.append(nx)
                count += 1
                
    return count

def solution(n, wires):
    answer = float("INF")
    tree = defaultdict(list)

    for u, v in wires:
        tree[u].append(v)
        tree[v].append(u)
        
    for u, v in wires:
        tree[u].remove(v)
        tree[v].remove(u)
        
        cnt_u = dfs(u, tree)
        cnt_v = n - cnt_u
        
        diff = abs(cnt_u - cnt_v)
        answer = min(answer, diff)
        
        tree[u].append(v)
        tree[v].append(u)
        
    return answer