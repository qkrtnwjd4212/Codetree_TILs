n, m = map(int, input().split())

arr1 = [0] * 1000000
time1 = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        arr1[time1] = arr1[time1 - 1] + v
        time1 += 1

arr2 = [0] * 1000000
time2 = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        arr2[time2] = arr2[time2 - 1] + v
        time2 += 1

# 매 시간별 선두 체크
change = 0
prev = ''
for i in range(1, time1):
    # A가 선두면서 이전 선두는 A가 아님 (선두 바뀜)
    if arr1[i] > arr2[i] and prev != 'A':
        prev = 'A'
        change += 1
    
    # B가 선두면서 이전 선두는 B가 아님 (선두 바뀜)
    elif arr1[i] < arr2[i] and prev != 'B':
        prev = 'B'
        change += 1
    
    # A, B가 동시에 선두면서 이전 선두는 AB가 아님 (선두 바뀜)
    elif arr1[i] == arr2[i] and prev != 'AB':
        prev = 'AB'
        change += 1

print(change)