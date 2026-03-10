n = int(input())
x = []
dir = []

for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

arr = [0] * 2001
cur = 0
cnt = 0

for i in range(n):
    if dir[i] == 'R':
        nx = cur + x[i]
    else:
        nx = cur - x[i]
    
    for i in range(min(cur, nx) + 1000, max(cur, nx) + 1000):
        arr[i] += 1
    cur = nx

for x in arr:
    if x >= 2:
        cnt += 1

print(cnt)

