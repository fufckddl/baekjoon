# 문자열 입력받기 (앞뒤 공백 제거)
string = input().strip()

# 빈 문자열인 경우 단어 개수는 0
if string == '':
    print(0)
else:
    # 공백을 기준으로 문자열을 분리하여 단어 리스트 생성
    words = string.split()
    # 단어 개수 출력
    print(len(words))