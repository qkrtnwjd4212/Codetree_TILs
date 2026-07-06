n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

arr = [[0] * 201 for _ in range(201)]

for i in range(n):
    for a in range(x[i], x[i] + 8):
        for b in range(y[i], y[i] + 8):
            arr[a][b] = 1

res = sum(sum(row) for row in arr)
print(res)