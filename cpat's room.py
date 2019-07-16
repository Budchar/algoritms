n = int(input())
k = input().split()
d = dict()
for i in k:
    d[i] = d.get(i, 0) + 1

for key, val in d.items():
    if val == 1:
        print(key)