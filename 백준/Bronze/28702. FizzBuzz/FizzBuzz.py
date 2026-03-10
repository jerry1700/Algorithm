fb = [input() for i in range(3)]
number = [x for x in fb if x.isdigit()]
num = number[0]
num_idx = fb.index(num)

if num_idx == 0:
    fb = [int(fb[num_idx]), int(fb[num_idx]) + 1, int(fb[num_idx]) + 2]
elif num_idx == 1:
    fb = [int(fb[num_idx]) - 1, int(fb[num_idx]), int(fb[num_idx]) + 1]
else:
    fb = [int(fb[num_idx]) - 2, int(fb[num_idx]) - 1, int(fb[num_idx])]

test = fb[-1] + 1

if test % 3 == 0 and test % 5 == 0:
    print("FizzBuzz")
elif test % 3 == 0 and test % 5 != 0:
    print("Fizz")
elif test % 3 != 0 and test % 5 == 0:
    print("Buzz")
else:
    print(test)
