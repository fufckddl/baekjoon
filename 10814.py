n = int(input())
lst = []
for i in range(n):
    data = list(map(str, input().split()))
    lst.append((int(data[0]), i, data[1]))

lst.sort(key = lambda x : (x[0], x[1]))

for age, _, name in lst:
    print(age, name)