n = int(input())

for i in range(n):
    a,b,x = list(map(int, input().split()))
    print(a*(x - 1) + b)