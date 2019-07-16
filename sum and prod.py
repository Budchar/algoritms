import numpy

n, m = map(int, input().split())
l = list()
for i in range(n):
    l.append(list(map(int, input().split())))

ls = numpy.sum(l, axis=0)
print(numpy.prod(ls))