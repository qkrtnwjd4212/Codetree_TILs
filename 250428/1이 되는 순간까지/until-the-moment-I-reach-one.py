N = int(input())

def f(n, cnt):
    #print(n)
    if n == 1:
        print(cnt)
        return 0

    if n % 2 == 0:
        f(n // 2, cnt + 1)
    else:
        f(n // 3, cnt + 1)

f(N, 0)