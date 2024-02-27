n = int(input())
shape = {}
for i in range(n):
    word = input().split()
    shape[word[0]] = word[1:]
thing = str(input())
for m in shape.keys():
    if thing in shape.setdefault(m):
        print(m)