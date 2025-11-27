import sys

n = int(input())
# 카운팅 정렬
count = [0] * 10001  # 1~10000까지의 수

# 입력받으면서 바로 카운트
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    count[num] += 1

# 카운트된 순서대로 출력 
for i in range(1, 10001):
    if count[i] > 0:
        sys.stdout.write((str(i) + "\n") * count[i])