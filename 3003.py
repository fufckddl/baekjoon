basic = [1, 1, 2, 2, 2, 8]
#킹 1개 퀸 1개 룩 2개 비숍 2개 나이트 2개 폰 8개
count = list(map(int, input().split()))
temp = []
for i in range(6):
    temp.append(basic[i] - count[i])
    print(temp[i], end = " ")
