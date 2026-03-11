n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

OFFSET = 100000
arr = [''] * (OFFSET * 2 + 1) 
cur = OFFSET

# 각 칸마다 BW,BWBW 이런 문자열로 저장한뒤 마지막에 색 검사하는 방식
for i in range(n):
    if dir[i] == 'R':
        for j in range(cur, cur + x[i]):
            arr[j] += 'B'
        cur += (x[i] - 1)
    else:
        for j in range(cur - x[i] + 1, cur + 1):
            arr[j] += 'W'
        cur -= (x[i] - 1)

# arr 돌면서 색 검사
for i in range(len(arr)):
    if arr[i].count('B') >= 2 and arr[i].count('W') >= 2:
        arr[i] = 'G'
    elif arr[i] != '':
        arr[i] = arr[i][-1]

b, w, g = 0, 0, 0
for color in arr:
    if color == 'B':
        b += 1
    elif color == 'W':
        w += 1
    elif color == 'G': 
        g += 1

print(w, b, g)