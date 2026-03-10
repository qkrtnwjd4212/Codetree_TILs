n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr = [0] * 201 

for i in range(n):
    a, b = segments[i]
    for j in range(a + 100, b + 100):
        arr[j] += 1

#print(arr)
print(max(arr))