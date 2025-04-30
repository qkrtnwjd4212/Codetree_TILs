n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b): # 최대공약수 
    if b == 0:
        return a
    
    return gcd(b, a % b)

def lcm(tmp_lcm, cnt):
    if cnt >= n:
        return tmp_lcm
    
    #print(tmp_lcm, cnt)
    next_lcm = tmp_lcm * arr[cnt] // gcd(tmp_lcm, arr[cnt])
    return lcm(next_lcm, cnt+1)

print(lcm(arr[0], 1))