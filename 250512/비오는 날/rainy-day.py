n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

class weather:
    def __init__(self, date, day, w):
        self.date = date
        self.day = day
        self.w = w 

weathers = [weather(d, dy, w) for d, dy, w in arr]

tmp = -1
for i, wt in enumerate(weathers):
    if wt.w == 'Rain' and tmp == -1:
        tmp = i
    elif wt.w == 'Rain' and wt.date < weathers[tmp].date:
        tmp = i

print(f"{weathers[tmp].date} {weathers[tmp].day} {weathers[tmp].w}")