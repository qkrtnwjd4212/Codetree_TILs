n = int(input())
word = [input() for _ in range(n)]

sorted_words = sorted(word)

for w in sorted_words:
    print(w, end='\n')