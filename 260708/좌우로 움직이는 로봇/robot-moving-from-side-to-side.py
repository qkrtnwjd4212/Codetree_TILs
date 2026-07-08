n, m = map(int, input().split())
arr1, arr2 = [0] * 2000000, [0] * 2000000

ta = 1
for _ in range(n):
    t, dir = input().split()

    for _ in range(int(t)):
        arr1[ta] = arr1[ta - 1] + (1 if dir == 'R' else -1)
        ta += 1

tb = 1
for _ in range(m):
    t, dir = input().split()

    for _ in range(int(t)):
        arr2[tb] = arr2[tb - 1] + (1 if dir == 'R' else -1)
        tb += 1

if ta < tb:
    for i in range(ta, tb):
        arr1[i] = arr1[i-1]
elif ta > tb:
    for i in range(tb, ta):
        arr2[i] = arr2[i-1]

res = 0
for i in range(1, max(ta, tb)):
    if arr1[i-1] != arr2[i-1] and arr1[i] == arr2[i]:
        res += 1
    
print(res)