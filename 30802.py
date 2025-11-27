import math

n = int(input())  # 참가자 수

# 티셔츠 사이즈별 참가자 수
sizes = list(map(int, input().split()))

# 티셔츠 묶음 단위 t, 펜 묶음 단위 p
t, p = map(int, input().split())

# 티셔츠 묶음 수 계산 (각 사이즈별로 필요한 수량을 t로 나눈 올림값의 합)
t_shirt_bundles = 0
for size in sizes:
    t_shirt_bundles += math.ceil(size / t)

# 펜 묶음 수와 낱개 수 계산
pen_bundles = n // p
pen_singles = n % p

# 출력
print(t_shirt_bundles)
print(pen_bundles, pen_singles)
