n = int(input())
dir, dist = [], []
for _ in range(n):
    a, b = input().split()
    dir.append(a)
    dist.append(int(b))

direction = {
    'N': 0,
    'E': 1,
    'W': 2,
    'S': 3
}

dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

x, y = 0, 0
time = 0
check = 0
for i in range(n):
    for _ in range(dist[i]):
        dir_num = direction[dir[i]]
        x += dx[dir_num]
        y += dy[dir_num]
        time += 1

        if x == 0 and y == 0:
            print(time)
            check = 1
            exit()

if check == 0:
    print(-1)

