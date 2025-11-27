array = []
for i in range(28):
   array.append(int(input()))

array.sort()
for i in range(1, 31):
    if i not in array:
        print(i)