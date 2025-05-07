n = int(input())
nums = list(map(int, input().split()))


for i in range(0, n, 2): # i = 0, 2, 4, 6, ...
    tmp = sorted(nums[:i+1])
    print(tmp[i//2], end=' ') # mean = 0, 1, 2, 3, ...

