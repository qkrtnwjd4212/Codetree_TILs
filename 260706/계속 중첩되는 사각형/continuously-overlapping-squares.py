n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

arr = [[0] * 201 for _ in range(201)]

for i in range(n):
    color = i % 2 # 0이면 빨강, 1이면 파랑
    for x in range(x1[i] + 100, x2[i] + 100):
        for y in range(y1[i] + 100, y2[i] + 100):
            if color == 1: # 파랑일때만 색칠
                arr[x][y] = 1
            else:
                arr[x][y] = 0

res = sum(sum(row) for row in arr)
print(res)