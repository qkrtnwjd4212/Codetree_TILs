n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 오, 아, 왼, 위
x, y = 0, 0 #시작점
dir = 0 # 시작 방향 - 오른쪽

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m 

arr[x][y] = 1
for i in range(2, n * m + 1):
    nx, ny = x + dx[dir], y + dy[dir]
 
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir = (dir + 1) % 4
    
    x, y = x + dx[dir], y + dy[dir]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()