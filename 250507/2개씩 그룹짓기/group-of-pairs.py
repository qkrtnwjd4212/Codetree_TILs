n = int(input())
nums = list(map(int, input().split()))

nums.sort()
max_num = []

for i in range(n):
    max_num.append(nums[i] + nums[2*n-i-1])

print(max(max_num))
