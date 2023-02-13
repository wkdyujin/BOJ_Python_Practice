n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0, 0] + [float("inf")] * (n - 1) # n번째로 갈 수 있는 최소 점프 수 (1번째는 항상 0)

for i in range(2, n + 1): # dp(n)을 찾기 위해 반복
    for j in range(1, i + 1): # i: 도달해야 하는 곳 / j: 현재위치
        if(arr[j] >= i - j): # 현재 갈 수 있는 거리(arr[j])가 i까지의 거리(i-j)보다 같거나 커야
            minJump = dp[j] + 1
            if(dp[i] > minJump):
                dp[i] = minJump
                
if(dp[n] == float("inf")):
    print(-1)
else:
    print(dp[n])