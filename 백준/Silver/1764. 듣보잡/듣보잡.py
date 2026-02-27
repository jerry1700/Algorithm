N, M = map(int, input().split())
listen = {input() for i in range(N)}
look = {input() for i in range(M)}

listen_look = listen & look

print(len(listen_look))
print("\n".join(sorted(list(listen_look))))
