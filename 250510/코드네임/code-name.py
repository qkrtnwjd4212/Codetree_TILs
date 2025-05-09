
class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = []
for i in range(5):
    name, score = input().split()
    score = int(score)
    
    students.append(student(name, score))

mini = 100
ans = ""
for i in range(5):
    if students[i].score < mini:
        mini = students[i].score 
        ans = students[i].name 

print(f"{ans} {mini}")