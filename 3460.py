t = int(input()) #테스트 케이스 수

for i in range(t):
    n = int(input())
    b = bin(n)
    for j in range(0, len(b[2:])):
        if(list(reversed(b[2:]))[j] == '1'):
            print(j, end=' ')