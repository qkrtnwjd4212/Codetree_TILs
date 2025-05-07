n, k, t = input().split()
n, k = int(n), int(k)
words = [input() for _ in range(n)]

t_word = []
l = len(t)
for word in words:
    #print(word[:l])
    if word[:l] == t:
        t_word.append(word)

t_word = sorted(t_word)
print(t_word[k-1])