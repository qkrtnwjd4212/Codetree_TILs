n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

arr = [''] * 10000
cur = 5000

for i in range(n):
    if dir[i] == 'L':
        for cnt in range(x[i]):
            arr[cur] = 'W'
            cur -= 1
        cur += 1
    else:
        for cnt in range(x[i]):
            arr[cur] = 'B'
            cur += 1
        cur -= 1

print(arr.count('W'), arr.count('B'))