n = int(input())
students = []

class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


for _ in range(n):
    n_i, h_i, w_i = input().split()
    students.append(student(n_i, int(h_i), int(w_i)))

students.sort(key=lambda x:(x.height, -x.weight))

for i in range(n):
    print(students[i].name, students[i].height, students[i].weight)