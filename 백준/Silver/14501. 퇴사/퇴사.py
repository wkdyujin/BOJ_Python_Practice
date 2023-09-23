N = int(input())
arr = []
for i in range(N):
    t, p = map(int, input().split())
    arr.append([t, p])

max_p = 0 # 결과

def f(n, cur_p, end_n):
    global max_p
    if(n < 0):
        return
    
    if(n + arr[n][0] - 1 <= end_n):
        max_p = max(max_p, cur_p)
        for i in range(n-1, -1, -1):
            f(i, cur_p + arr[i][1], n-1) # (4, 20, n)
    else:
        max_p = max(max_p, cur_p - arr[n][1])
            
for i in range(N-1, -1, -1):
    f(i, arr[i][1], N - 1)
    
print(max_p)