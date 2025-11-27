# 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용
# 한대의 노트북 생산에 재료비 인건비 등 총 B만원의 가변 비용

# ex) A = 1000, B = 70,일 경우 한대 생산에는 총 1070만원

# 노트북 가격이 C만원으로 책정되어 있을 때, 총 수입이 총 비용을 넘어서는 최초의 시점
# 총비용 = A + B * 노트북 생산 개수
# 총수입 = C * 노트북 생산 개수

#손익분기점 계산 함수 정의
def calculate_break_even_point(a, b, c):
    if b >= c:
        return -1
    return a // (c - b) + 1

if __name__ == "__main__":
    import sys

    a, b, c = map(int, sys.stdin.readline().split())
    print(calculate_break_even_point(a, b, c))