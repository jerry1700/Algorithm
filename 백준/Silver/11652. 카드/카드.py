N = int(input())
nums = sorted([int(input()) for _ in range(N)])

cnt = 0
mxval = -(2 ** 62) - 1
mxcnt = 0

for i in range(N):
    if i == 0 or nums[i - 1] == nums[i]:
        cnt += 1
    else:
        if cnt > mxcnt:
            mxval = nums[i - 1]
            mxcnt = cnt
        cnt = 1

if cnt > mxcnt:
    mxval = nums[i - 1]

print(mxval)