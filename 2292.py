n = int(input())
layer = 1
max_num = 1

while max_num < n:
    max_num += 6 * layer
    layer += 1
print(layer)