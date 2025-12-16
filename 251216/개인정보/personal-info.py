n = int(5)
studendts = []

class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    n_, h, w = input().split()
    studendts.append(student(n_, int(h), float(w)))

print('name')
studendts.sort(key=lambda x: x.name)
for i in range(n):
    print(studendts[i].name, studendts[i].height, studendts[i].weight)

print('')
print('height')
studendts.sort(key=lambda x: -x.height)
for i in range(n):
    print(studendts[i].name, studendts[i].height, studendts[i].weight)