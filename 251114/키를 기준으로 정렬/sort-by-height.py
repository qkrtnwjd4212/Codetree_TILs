n = int(input())
arr = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    arr.append((n_i, h_i, w_i))

arr.sort(lambda x: x[1])

for i in range(n):
    n, h, w = arr[i]
    print(n, h, w)