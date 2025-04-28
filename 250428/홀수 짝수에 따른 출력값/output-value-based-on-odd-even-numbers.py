N = int(input())

def f(n):
    if n == 1 or n == 2:
        return n 
    
    if n % 2 == 0:
        return f(n-2) + n 
    else:
        return f(n-2) + n 
    
print(f(N))
