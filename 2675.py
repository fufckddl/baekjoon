str = int(input())#입력받을 문자열 수
results = []
for i in range(str):
    r = input().split()
    # 한번에 저장
    result = ''.join([int(r[0]) * char for char in r[1]])
    results.append(result)

# 반복문이 끝난 후 모든 결과 출력
for result in results:
    print(result)

