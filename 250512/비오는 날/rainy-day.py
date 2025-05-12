n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

class weather:
    def __init__(self, date, day, w):
        self.date = date
        self.day = day
        self.w = w 

weathers = [weather(d, dy, w) for d, dy, w in arr]

for i in range(n):
    if weathers[i].w == 'Rain':
        print(f"{weathers[i].date} {weathers[i].day} {weathers[i].w}")
        break
