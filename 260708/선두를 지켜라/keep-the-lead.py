n, m = map(int, input().split())

# Process A's movements
arr1 = [0] * 1000000
d1, cnt1 = 0, 0
for _ in range(n):
    vi, ti = map(int, input().split())
    
    for i in range(ti):
        d1 += vi
        cnt1 += 1
        arr1[cnt1] = d1

# Process B's movements
arr2 = [0] * 1000000
d2, cnt2 = 0, 0
for _ in range(m):
    vi, ti = map(int, input().split())
    
    for i in range(ti):
        d2 += vi
        cnt2 += 1
        arr2[cnt2] = d2

# print(arr1)
# print(arr2)

cnt = 1
prev_leader = 0
leader = 0
res = 0
while arr1[cnt] > 0 or arr2[cnt] > 0:

    if arr1[cnt] > arr2[cnt]:
        leader = 1
        if prev_leader == 2:
            res += 1
            prev_leader = 1
    elif arr1[cnt] < arr2[cnt]:
        leader = 2
        if prev_leader == 1:
            res += 1
            prev_leader = 2
    prev_leader = leader
    cnt += 1

print(res)