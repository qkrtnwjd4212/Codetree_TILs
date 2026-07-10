# 클래스 선언
class Shake:
    def __init__(self, time, person1, person2):
        self.time, self.person1, self.person2 = time, person1, person2
    
# 변수 선언 및 입력
n, k, p, t = tuple(map(int, input().split())) # n명, 전염 가능 횟수 k, 초기전염자 p, t번 
shakes = []
for _ in range(t):
    time, person1, person2 = tuple(map(int, input().split()))
    shakes.append(Shake(time, person1, person2))

shake_num = [0] * (n+1)
infected = [False] * (n+1)
infected[p] = True 

shakes.sort(key = lambda x: x.time)

# 각 악수 횟수 체크
for shake in shakes:
    target1 = shake.person1
    target2 = shake.person2

    # 감염되어 있을 경우 -> 악수 횟수 증가
    if infected[target1]:
        shake_num[target1] += 1
    if infected[target2]:
        shake_num[target2] += 1    

    # 악수횟수 체크해서 감염시키기 
    if shake_num[target1] <= k and infected[target1]:
        infected[target2] = True
    if shake_num[target2] <= k and infected[target2]:
        infected[target1] = True

for i in range(1, n+1):
    if infected[i]:
        print(1, end="")
    else:
        print(0, end="")