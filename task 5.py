def count_grandson(tree, parent):
    if parent not in tree:
        return 0
    else:
        grandson = len(tree[parent])
        for child in tree[parent]:
            grandson += count_grandson(tree, child)
        return grandson

n = int(input())
tree = {}
for i in range(n):
    name = input().split()
    if name[0] not in tree:
        tree[name[0]] = [name[1]]
    else:
        tree[name[0]].append(name[1])
parent = str(input())
print(count_grandson(tree, parent))
