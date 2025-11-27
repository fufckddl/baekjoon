n = int(input())
# N개의 정수를 한 줄에 입력받기 (최대 N개까지만)
num = list(map(int, input().split()))[:n]
k = int(input())
count = 0
# N개만큼 반복
for i in range(n):
    if num[i] == k:
        count +=1

print(count)