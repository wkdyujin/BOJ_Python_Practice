import sys

n = int(sys.stdin.readline())
dp = []

for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    dp.append(arr)

for i in range(1, n): # 2번째부터 시작
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0] # 빨간색을 골랐을 때 최소 -> 이전의 파랑/초록 중 최소 + 빨강 가격
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1] # 초록색 ''
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2] # 파랑색 ''
    
print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))