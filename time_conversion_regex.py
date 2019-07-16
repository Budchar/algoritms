import re

regex = re.compile(r'([0-1][0-9])([:][0-6][0-9][:][0-6][0-9])([AM]|[PM])', re.I)
s = regex.match(input())
print(s)