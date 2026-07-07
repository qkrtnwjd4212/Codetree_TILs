n, m = map(int, input().split())

d1 = []
t1 = []
arr1 = [0] * 1000000
for _ in range(n):
    direction, time = input().split()
    d1.append(direction)
    t1.append(int(time))
 
d2 = []
t2 = []
arr2 = [0] * 1000000
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# ==============================
idx1, cur1 = 0, 0
for i in range(n):
    for j in range(t1[i]):
        arr1[idx1] = cur1
        if d1[i] == 'R':
            cur1 += 1
        elif d1[i] == 'L':
            cur1 -= 1
        idx1 += 1

idx2, cur2 = 0, 0
for i in range(m):
    for _ in range(t2[i]):
        arr2[idx2] = cur2
        if d2[i] == 'R':
            cur2 += 1
        elif d2[i] == 'L':
            cur2 -= 1
        idx2 += 1

res = -1
cnt = max(sum(t1), sum(t2))
for i in range(1, cnt):
    if arr1[i] == arr2[i]:
        res = i
        break

# print(arr1[:20])
# print(arr2[:20])

print(res)
