m1, d1, m2, d2 = map(int, input().split())
A = input()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

diff = (sum(num_of_days[:m2]) + d2) - (sum(num_of_days[:m1]) + d1)

ans = diff // 7
if days[A] <= diff % 7:
    ans += 1 

print(ans)