n = int(input())

points = [(int(i+1), tuple(map(int, input().split()))) for i in range(n)]
points.sort(key=lambda x: (x[1][0] + x[1][1]))
for i in range(n):
    print(points[i][0])

# class point:
#     def __init__(self, idx, x, y):
#         self.idx = idx 
#         self.x = x
#         self.y = y

# points = []
# for i in range(n):
#     x_, y_ = input().split()
#     points.append(point(i+1, x_, y_))


