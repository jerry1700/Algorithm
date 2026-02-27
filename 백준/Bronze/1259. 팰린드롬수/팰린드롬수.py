while True:
    palindrome_test = int(input())
    if palindrome_test == 0:
        break

    palindrome_test = str(palindrome_test)

    if len(palindrome_test) == 1:
        print("yes")
    else:
        for i in range(len(palindrome_test) // 2):
            if palindrome_test[i] == palindrome_test[len(palindrome_test) - 1 - i]:
                pass
            else:
                print("no")
                break
            if i == len(palindrome_test) // 2 - 1:
                print("yes")
