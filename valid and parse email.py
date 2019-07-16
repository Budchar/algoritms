# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    name, adress = input().split()
    e = re.match(r'<[a-zA-Z]+(\w|-|_|\.)*@[a-zA-Z]+\.[a-zA-Z]{1,3}>', adress)
    if e:
        print(name, adress)
