commands = list(input())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir = 0
time = 0
ans = -1

for com in commands:
    if com == 'F':
        x += dx[dir]
        y += dy[dir]
    elif com == 'L':
        dir = (dir + 3) % 4
    elif com == 'R':
        dir = (dir + 1) % 4
    
    time += 1
    if x == 0 and y == 0:
        ans = time
        break

print(ans)
