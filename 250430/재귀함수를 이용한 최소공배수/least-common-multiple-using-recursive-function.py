n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b): # 최대공약수 
    if b == 0:
        return a
    
    return gcd(b, a % b)

def lcm(a, b, cnt):
    if cnt == n - 1:
        return a
    
    tmp_lcm = gcd(a, b) * a * b
    #print(tmp_lcm)
    return lcm(tmp_lcm, arr[cnt+1], cnt+1)

print(lcm(arr[0], arr[1], 1))