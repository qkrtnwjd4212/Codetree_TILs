num = int(input())

def print_1_to_n(n):
    if n == 0:
        return

    print_1_to_n(n-1)
    print(n, end=" ")

def print_n_to_1(n):
    if n == 0:
        return

    print(n, end=" ")
    print_n_to_1(n-1)

print_1_to_n(num)
print()
print_n_to_1(num)