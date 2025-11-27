c = int(input()) # 손님 수

for i in range(c):
    w, h, n = list(map(int, input().split()))

    floor = n % w if n % w != 0 else w
    room = (n - 1) // w + 1
    print(str(floor) + str(room).zfill(2))
    # w = 6
    # h = 12
    # n = 10 번째 온 손님
    # 층수 = n % w 
    # 호수 = n // w + 1