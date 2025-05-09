user2_id, user2_level = input().split()
user2_level = int(user2_level)

class user:
    def __init__(self, uid, level):
        self.uid = uid
        self.level = level 

user1 = user("codetree", 10)
user2 = user(user2_id, user2_level)

print(f"user {user1.uid} lv {user1.level}")
print(f"user {user2.uid} lv {user2.level}")
