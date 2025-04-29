N = int(input())

def seq(n):
    if n == 1 or n == 2:
        return n  

    return seq(n // 3) + seq(n-1)

print(seq(N))

    