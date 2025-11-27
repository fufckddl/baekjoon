n = int(input())
result = 0

for i in range(1, n):
    digit_sum = sum(map(int, str(i)))
    if i + digit_sum == n:
        result = i
        break

print(result)