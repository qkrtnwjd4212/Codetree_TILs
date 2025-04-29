n = int(input())
arr = list(map(int, input().split()))

def f(i, max_num):
    if i == n:
        return max_num
    
    if arr[i] > max_num:
        return f(i+1, arr[i])
    else:
        return f(i+1, max_num)

print(f(0, 0))