n = int(input())

# points = [(int(i+1), tuple(map(int, input().split()))) for i in range(n)]
# points.sort(key=lambda x: (abs(x[1][0]) + abs(x[1][1])))
# for i in range(n):
#     print(points[i][0])

class point:
    def __init__(self, idx, x, y):
        self.idx = int(idx)
        self.x = int(x)
        self.y = int(y)

points = []
for i in range(n):
    x_, y_ = input().split()
    points.append(point(i+1, x_, y_))

points.sort(key=lambda x: (abs(x.x) + abs(x.y)))
for i in range(n):
    print(points[i].idx)

