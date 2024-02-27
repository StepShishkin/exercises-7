n = int(input())
all_word = []
for i in range(n):
    word = input().split()
    all_word.append(word)
antonym = dict(all_word)
new_word = str(input())
if new_word in antonym:
    print(antonym[new_word])
else:
    for m in antonym.keys():
        if antonym.setdefault(m) == new_word:
            print(m)
