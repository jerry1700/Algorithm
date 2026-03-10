L = int(input())
password = input()
hashword = 0

for i in range(L):
    hashword += (ord(password[i]) - 96) * 31 ** i

print(hashword % 1234567891)
