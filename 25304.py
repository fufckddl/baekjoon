x = int(input()) #금액
n = int(input()) #종류 수
all = 0
result = []
for i in range(n):
    receipt = list(map(int, input().split())) #가격 갯수 (공백 분리)

    price = receipt[0] #가격
    count = receipt[1] #갯수
    result.append(price * count)

for i in range(n):
    all += result[i]

if (all == x):
    print("Yes")
else:
    print("No")
