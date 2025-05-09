secret_code, meeting_point, time = input().split()
time = int(time)

class secret:
    def __init__(self, code, meeting, time):
        self.code = code
        self.meeting = meeting
        self.time = time
    
secret1 = secret(secret_code, meeting_point, time)
print(f"secret code : {secret1.code}")
print(f"meeting point : {secret1.meeting}")
print(f"time : {secret1.time}")
