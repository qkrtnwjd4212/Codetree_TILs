h, m, h2, m2 = map(int, input().split())

cnt = 0

while not (h == h2 and m == m2):
    #print(h, m)
    m += 1
    cnt += 1

    if m == 60:
        h += 1
        m = 0

print(cnt)