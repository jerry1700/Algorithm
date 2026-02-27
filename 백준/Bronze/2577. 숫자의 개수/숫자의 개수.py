A = int(input())
B = int(input())
C = int(input())
ABC = A * B * C
ABC = str(ABC)

num = [0] * 10

for i in range(len(ABC)):
    num[int(ABC[i])] += 1

for i in num:
    print(i)
