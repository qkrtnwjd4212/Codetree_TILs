m1, d1, m2, d2 = map(int, input().split())

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 == m2 and d1 == d2:
    print(1)
else:
    print((sum(num_of_days[:m2]) + d2) - (sum(num_of_days[:m1]) + d1))

