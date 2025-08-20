a, b, c = map(int, input().split())

if not (a >= 11 and b >= 11 and c >= 11):
    print(-1)
else:
    prev = (11 * 24 * 60) + (11 * 60) + 11
    now = (a * 24 * 60) + (b * 60) + c
    print(now - prev)