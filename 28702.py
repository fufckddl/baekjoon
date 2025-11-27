def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

# 3개의 입력 받기
inputs = []
for i in range(3):
    inputs.append(input())

# 숫자를 찾아서 다음 숫자 계산
next_num = None
for i in range(3):
    if inputs[i].isdigit():
        # 숫자를 찾았으면, 그 위치에서 다음 숫자 계산
        # i번째 위치면 (3-i)만큼 더해야 다음 숫자가 됨
        next_num = int(inputs[i]) + (3 - i)
        break

# 다음 숫자의 FizzBuzz 결과 출력
if next_num is not None:
    result = fizzbuzz(next_num)
    print(result)