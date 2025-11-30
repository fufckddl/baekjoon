n = int(input())
data = set(map(int, input().split()))

m = int(input())
data2 = list(map(int, input().split()))

for num in data2:
    print(1 if num in data else 0)