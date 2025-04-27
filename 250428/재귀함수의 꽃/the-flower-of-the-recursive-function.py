N = int(input())

def print_n_to_1_to_n(n):
    if n == 0:
        return

    print(n, end = " ")
    print_n_to_1_to_n(n-1)
    print(n, end = " ")

print_n_to_1_to_n(N)
