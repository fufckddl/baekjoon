while True:
    a = list(map(int, input().split()))
    if a[0] > a[1] and a[0] > a[2]:
        v = a[0] ** 2
        w = a[1] ** 2
        h = a[2] ** 2
        if v == w+h:
            print("right")
        else:
            print("wrong")
    elif a[1] > a[0] and a[1] > a[2]:
        v = a[1] ** 2
        w = a[0] ** 2
        h = a[2] ** 2
        if v == w+h:
            print("right")
        else:
            print("wrong")
    elif a[2] > a[0] and a[2] > a[1]:
        v = a[2] ** 2
        w = a[0] ** 2
        h = a[1] ** 2
        if v == w+h:
            print("right")
        else:
            print("wrong")
    elif a[0] == 0:
        break


    # 지피티 답변 (더 쉬운 방법)
    #if a[0] == 0:
    #    break
    
    #a.sort()  # 오름차순 정렬
    #if a[0]**2 + a[1]**2 == a[2]**2:
    #    print("right")
    #else:
    #    print("wrong")