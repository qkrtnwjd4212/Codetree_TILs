unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

bomb1 = bomb(unlock_code, wire_color, seconds)
print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.sec}")