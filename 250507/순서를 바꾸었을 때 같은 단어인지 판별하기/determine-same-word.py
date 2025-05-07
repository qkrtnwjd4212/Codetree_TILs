word1 = input()
word2 = input()

sorted_w1 = sorted(word1)
sorted_w2 = sorted(word2)

ans = sorted_w1 == sorted_w2
if ans:
    print("Yes")
else:
    print("No")
    

