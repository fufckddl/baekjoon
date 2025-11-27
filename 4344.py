c = int(input())
percent = []
for i in range(c):
    data = list(map(int, input().split()))
    n = data[0]  # 학생 수
    scores = data[1:]  # 점수들
    
    # 평균 계산
    average = sum(scores) / n
    
    # 평균을 넘는 학생 수 계산
    above_average = sum(1 for score in scores if score > average)
    
    # 비율 계산 및 출력 (소수점 셋째 자리까지)
    ratio = (above_average / n) * 100
    percent.append(ratio)

for ratio in percent:
    print(f"{ratio:.3f}%")