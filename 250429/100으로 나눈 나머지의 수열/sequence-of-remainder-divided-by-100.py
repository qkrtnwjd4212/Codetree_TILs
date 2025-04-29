N = int(input())

def f(n1, n2, cnt):
    if cnt == N:
        return n1

    num = (n1 * n2) % 100
    return f(n2, num, cnt+1)    

print(f(2, 4, 1))