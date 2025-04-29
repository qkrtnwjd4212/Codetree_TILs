a, b, c = map(int, input().split())
num = a * b * c

def f(n, total):
    if n < 10:
        return total + n

    return f(n // 10, total + (n % 10))

print(f(num, 0))