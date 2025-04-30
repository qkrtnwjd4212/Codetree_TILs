n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b): # 최대공약수 
    if b == 0:
        return a
    
    return gcd(b, a % b)

def lcm(tmp_lcm, cnt):
    if cnt >= n - 1:
        return tmp_lcm
    
    #print(tmp_lcm, cnt)
    next_lcm = gcd(tmp_lcm, arr[cnt]) * tmp_lcm * arr[cnt]
    return lcm(next_lcm, cnt+1)

print(lcm((gcd(arr[0], arr[1]) * arr[0] * arr[1]), 2))