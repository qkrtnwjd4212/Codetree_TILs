n = int(input())
arr = []

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math 

for _ in range(n):
    name, k, e, m = input().split()
    arr.append(Student(name, int(k), int(e), int(m)))

arr.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for s in arr:
    print(s.name, s.kor, s.eng, s.math)
