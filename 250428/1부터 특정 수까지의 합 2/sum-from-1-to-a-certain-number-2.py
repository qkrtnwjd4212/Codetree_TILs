n = int(input())

def sum_1_to_n(n):
    if n == 1:
        return 1
    return sum_1_to_n(n-1) + n 

print(sum_1_to_n(n))