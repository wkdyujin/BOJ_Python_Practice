n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
cur_sum, end = 0, 0

for start in range(n):
    while(cur_sum < m and end < n):
        cur_sum += arr[end]
        end += 1
    if(cur_sum == m):
        res += 1
    cur_sum -= arr[start]
        
print(res)