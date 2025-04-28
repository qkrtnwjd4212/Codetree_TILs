N = int(input())

def fiv(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fiv(n-2) + fiv(n-1)

print(fiv(N))