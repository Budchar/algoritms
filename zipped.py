n, m = map(int, input().split())
a =[]
for _ in range(m):
    a.append(list(map(float,input().split())))

for i in zip(*a):
    print(sum(i)/len(i))