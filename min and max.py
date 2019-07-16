import numpy

n, m = map(int, input().split())
l = list()
for i in range(n):
    l.append(list(map(int, input().split())))

# axis = 0은 세로로 확인, 1이면 가로로 확인
# [[1,2][3,4]] 0일떈 1,3 2,4 비교 1일땐 1,2 3,4 비교
ls = numpy.min(l, axis=1)
print(numpy.max(ls))