n = int(input())
result = [0] * n;
for i in range(n):
    case = input().strip()
    count = 0
    for j in range(len(case)):
        if case[j] == 'o' or case[j] == 'O':
            count += 1
            result[i] += count
        else:
            count = 0
for i in range(len(result)):
    print(result[i])