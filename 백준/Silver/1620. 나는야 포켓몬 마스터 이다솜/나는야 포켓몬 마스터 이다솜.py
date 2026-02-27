N, M = map(int, input().split())
book = {}

for i in range(N):
    book[input()] = f"{i + 1}"
    
reverse_book = {v: k for k, v in book.items()}

for i in range(M):
    po = input()
    output = book.get(po)
    if output == None:
        print(reverse_book.get(po))
    else:
        print(output)
