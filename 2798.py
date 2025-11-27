count, m = map(int, input().split())

cardNum = list(map(int, input().split()))

max_sum = 0

# 3중 반복문으로 모든 3장의 카드 조합 확인
for i in range(len(cardNum)):
    for j in range(i + 1, len(cardNum)):
        for k in range(j + 1, len(cardNum)):
            current_sum = cardNum[i] + cardNum[j] + cardNum[k]
            # M을 넘지 않으면서 최대값 갱신
            if current_sum <= m and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)
