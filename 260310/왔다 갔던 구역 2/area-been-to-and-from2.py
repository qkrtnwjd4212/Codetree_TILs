n = int(input())
x = []
dir = []

for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

arr = [0] * (n * 10 * 2 + 1)
cur = 0
cnt = 0

for i in range(n):
    if dir[i] == 'R':
        for j in range(cur + 10, cur + x[i] + 10):
            arr[j] += 1
        cur += x[i]
    else:
        for j in range(cur + 10, cur - x[i] + 10, -1):
            arr[j] += 1
        cur -= x[i]

for x in arr:
    if x >= 2:
        cnt += 1

print(cnt)

