import re
for _ in range(int(input())):
    reg = re.finditer(r'[\s:]#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})', input())
    for r in reg:
        print(r.group()[1:]) 