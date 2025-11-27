n = list(map(int, input().split()))

temp = (n[0] ** 2) + (n[1] ** 2) + (n[2] ** 2) + (n[3] ** 2) + (n[4] ** 2)

print(temp%10)