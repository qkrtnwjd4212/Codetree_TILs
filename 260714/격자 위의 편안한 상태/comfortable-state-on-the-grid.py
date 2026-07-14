n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
arr = [[0] * (n+1) for _ in range(n+1)] # 0이면 빈칸, 1이면 색칠된칸 

def in_range(x, y):
    return 0 < x <= n and 0 < y <= n

for i in range(m):
    x, y = points[i]
    arr[x][y] = 1

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)