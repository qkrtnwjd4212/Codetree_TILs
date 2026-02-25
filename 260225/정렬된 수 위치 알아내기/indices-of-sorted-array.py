n = int(input())
nums = [[int(x), i, 0] for i, x in enumerate(input().split(), start=1)]

nums.sort(key=lambda x: x[0])
for i in range(n):
    nums[i][2] = i+1

nums.sort(key=lambda x: x[1])
for i in range(n):
    print(nums[i][2], end=' ')