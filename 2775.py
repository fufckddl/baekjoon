# a = 3
# b = 2
# 3층 2호 (302호)
#에 살기 위해서는 
#2(a-1)층의 1호부터 2(b)호까지 사람들의 수의 합 만큼사람을 데려와 살아야함
#0층의 1호는 1명, 2호는 2명 ... i호는 i명

#ex) 1층의 3호면
# -> 0층의 1호, 2호, 3호 인원의 합

#ex) 2층의 3호면
# -> 1층의 1호, 2호, 3호 인원의 합


t = int(input())

for _ in range(t):
    k = int(input())  # 층수
    n = int(input())  # 호수
    
    # DP 테이블: dp[층][호]
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 0층 초기화: 0층 i호에는 i명
    for i in range(1, n + 1):
        dp[0][i] = i
    
    # 각 층별로 계산
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            # k층 n호 = k층 (n-1)호 + (k-1)층 n호
            dp[floor][room] = dp[floor][room - 1] + dp[floor - 1][room]
    
    print(dp[k][n])


#4층 1 6 21
#3층 1 5 15
#2층 1 4 10
#1층 1 3 6
#0층 1 2 3 