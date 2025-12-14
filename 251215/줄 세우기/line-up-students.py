n = int(input())
# 키, 몸무게, (번호)
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

students.sort(key=lambda x: (-x[0], -x[1], x[2]))

for h, w, i in students:
    print(h, w, i, end=' ')
    print('')