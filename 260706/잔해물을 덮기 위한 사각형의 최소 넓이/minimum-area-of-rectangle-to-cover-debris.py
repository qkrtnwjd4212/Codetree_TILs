x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split()) # 첫번째 직사각형
x1[1], y1[1], x2[1], y2[1] = map(int, input().split()) # 두번째 직사각형

arr = [[0] * 2001 for _ in range(2001)]
for x in range(x1[0]+1000, x2[0]+1000):
    for y in range(y1[0]+1000, y2[0]+1000):
        arr[x][y] = 1

for x in range(x1[1]+1000, x2[1]+1000):
    for y in range(y1[1]+1000, y2[1]+1000):
        arr[x][y] = 0

minx, miny = 2001, 2001
maxx, maxy = -1, -1

for x in range(2001):
    for y in range(2001):
        if arr[x][y] == 1:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)

res = (maxx - minx + 1) * (maxy - miny + 1)
if maxx == -1:
    print(0)
else:
    print(res)
