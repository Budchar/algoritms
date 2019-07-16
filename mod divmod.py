# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = int(input()), int(input())
print(str(int(a/b)), end="\n")
print(str(a%b), end="\n")
print(str(divmod(a,b)))
