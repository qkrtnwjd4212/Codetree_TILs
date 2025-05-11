n = int(input())
persons = []

for _ in range(n):
    name, address, city = input().split()
    persons.append((name, address, city))

class person:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

persons.sort(key=lambda x : x[0])
name, address, city = persons[-1]
person1 = person(name, address, city)

print(f"name {person1.name}")
print(f"addr {person1.address}")
print(f"city {person1.city}")

    
