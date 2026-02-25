# A진수로 표현된 N을 B진수로 변환해서 출력 
a, b = map(int, input().split())
n = list(map(int, input()))

# N을 10진수로 변환
num = 0
for i in range(len(n)):
    num = num * a + n[i]

# num을 B진수로 변환
digit = []
while True:
    if num < b:
        digit.append(num)
        break
    
    digit.append(num % b)
    num //= b

for i in digit[::-1]:
    print(i, end="")