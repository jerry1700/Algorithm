from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)

time = 0
while trucks:
    bridge.popleft()
    if trucks[0] + sum(bridge) <= L:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
    time += 1

while any(bridge):
    bridge.popleft()
    bridge.append(0)
    time += 1

print(time)