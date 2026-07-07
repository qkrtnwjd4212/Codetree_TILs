n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 1
same_num_cnt = []

for i in range(1, n):
    if arr[i-1] == arr[i]:
        cnt += 1
    else:
        same_num_cnt.append(cnt)
        cnt = 1
    
    if i == n-1:
        same_num_cnt.append(cnt)
    
if same_num_cnt:
    print(max(same_num_cnt))
else:
    print(1)