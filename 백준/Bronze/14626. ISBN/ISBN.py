isbn = list(input())

star_idx = isbn.index("*")

for i in range(10):
    isbn[star_idx] = i
    isbn = list(map(int, isbn))
    
    test = 0
    for j in range(len(isbn)):
        if j % 2 == 0:
            test += isbn[j]
        else:
            test += (isbn[j] * 3)
    
    if test % 10 == 0:
        break

print(i)
