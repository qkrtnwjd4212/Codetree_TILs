# n을 b진수로 변환 (4진수, 8진수)
n, b = map(int, input().split()) 

digit = []
while True:
    if n < b:
        digit.append(n)
        break
    
    digit.append(n % b)
    n //= b

for i in digit[::-1]:
    print(i, end="")