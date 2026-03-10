n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr = [0] * 100

for i in range(n):
    a, b = segments[i]
    for j in range(a, b+1):
        arr[j] += 1

print(max(arr))