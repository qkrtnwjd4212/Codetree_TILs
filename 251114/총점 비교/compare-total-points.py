n = int(input())
arr = []

class student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

for _ in range(n):
    n, k, e, m = input().split()
    arr.append(student(n, int(k), int(e), int(m)))

arr.sort(key=lambda x: (x.kor + x.eng + x.math))

for s in arr:
    print(s.name, s.kor, s.eng, s.math)