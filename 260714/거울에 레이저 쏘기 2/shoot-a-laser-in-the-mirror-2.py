n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
left = [3, 2, 1, 0] # \\ 
right = [1, 0, 3, 2] # / 

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

k_dir = (((k-1) // n) + 2) % 4 # 0(아래2), 1(왼3), 2(위0), 3(오1) 
kx, ky = 0, 0
dir_num = 1
for i in range(k-1):
    nx, ny = kx + dx[dir_num], ky + dy[dir_num]

    if not in_range(nx, ny):
        dir_num = (dir_num + 1) % 4
    else:
        kx, ky = nx, ny

cnt = 0
laser_dir = k_dir
while True:
    if arr[kx][ky] == '\\': # left
        laser_dir = left[laser_dir]
    else:
        laser_dir = right[laser_dir]
    
    nx, ny = kx + dx[laser_dir], ky + dy[laser_dir]
    if not in_range(nx, ny):
        print(cnt+1)
        break
    cnt += 1
    kx, ky = nx, ny

