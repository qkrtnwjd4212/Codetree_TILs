n, k = map(int, input().split())
blocks = [0] * n
arr = []

for i in range(k):
    a, b = map(int, input().split())
    arr.append([a, b])

for i in range(k):
    for cnt in range(arr[i][0], arr[i][1] + 1):
        blocks[cnt-1] += 1

#print(blocks)
print(max(blocks))