n = int(input())
a = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, m = input().split()
    b = set(map(int, input().split()))
    getattr(a, cmd)(b)

print(sum(a))