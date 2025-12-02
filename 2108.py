import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

# 1. 산술평균 (반올림)
print(round(sum(lst) / n))

# 2. 중앙값
print(lst[n // 2])

# 3. 최빈값
counter = Counter(lst)
modes = counter.most_common()
max_count = modes[0][1]
modes = [num for num, count in modes if count == max_count]
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])

# 4. 범위
print(lst[-1] - lst[0])