n = int(input())
lst = []
for i in range(n):
    k = input()
    lst.append(k)

array = list(set(lst)) #중복 제거
array.sort(key=lambda x : (len(x), x))

for i in range(len(array)):
    print(array[i])