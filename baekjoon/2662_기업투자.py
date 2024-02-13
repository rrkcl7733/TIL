N, M = map(int, input().split())

# 입력 중 투자 액수는 필요없다.
array = [list(map(int, input().split()))[1:] for _ in range(N)]

# N만원으로 M개의 회사에 투자해 얻을 수 있는 최대 이윤
dp = [[0] * M for _ in range(N)]

# 해당 dp 조건에서 M번 회사에 투자하는 비용
cost = [[0] * M for _ in range(N)]

# M = 0에서는 0번 회사에 몰빵해야한다.
for i in range(N):
    dp[i][0] = array[i][0]
    cost[i][0] = i+1

for i in range(N):
    for j in range(1, M):

        # 새로운 회사에 전재산 투자하는게 이득인 경우
        if dp[i][j-1] < array[i][j]:
            dp[i][j] = array[i][j]
            cost[i][j] = i+1
        else:
            dp[i][j] = dp[i][j-1]
            cost[i][j] = 0

        # 분산 투자가 이득인지 판단
        for k in range(i):
            if dp[i][j] < dp[k][j-1] + array[i-k-1][j]:
                cost[i][j] = i-k
                dp[i][j] = dp[k][j-1] + array[i-k-1][j]

# 최종 최대 이윤
print(dp[N-1][M-1])

# 얼마씩 투자했는지 확인한다.
r = N
result = []

# 최대 이윤에서 확인하므로 거꾸로 확인
# 0번 회사 투자금부터 출력이므로 왼쪽으로 append하겠다.
for j in range(M-1, -1, -1):

    # 투자금을 다 쓴거면 나머지는 0원 투자
    if not r:
        result.append(0)
    # 앞서 X원을 j번 회사에 투자했으면 dp[r-X][j-1] 크기를 확인
    else:
        result.append(cost[r-1][j])
        r -= cost[r-1][j]

print(*result[::-1])
