a, b, c = map(int, input().split())

prev = (11 * 24 * 60) + (11 * 60) + 11
now = (a * 24 * 60) + (b * 60) + c
if now - prev < 0:
    print(-1)
else:
    print(now - prev)