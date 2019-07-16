n, i = int(input()) ,list(map(int, input().split()))
print(all([all([j>0 for j in i]), n in i]))