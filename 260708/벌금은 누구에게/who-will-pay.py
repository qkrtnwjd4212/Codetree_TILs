# N 학생수, 벌칙 학생번호 M번, K번이상 벌칙 -> 벌금
N, M, K = map(int, input().split()) 
student = [int(input()) for _ in range(M)]

dict = {}
flag = 0
for num in student:
    if num in dict:
        dict[num] += 1
        if dict[num] == K:
            print(num)
            flag = 1
            break
    else:
        dict[num] = 1

if not flag:
    print(-1)



