N, K = map(int, input().split())
arr = list(map(int, input().split()))
max_e = 0

def f(idx, e, cur_k):
    global max_e
    
    if(cur_k >= K): # 소화해야 함
        e += cur_k-K
        cur_k = 0
    
    if(idx >= N): # 다 먹었을 때
        max_e = max(max_e, e)
        return
        
    if(0 < cur_k < K): # 먹어야 함
        f(idx+1, e, cur_k+arr[idx])
        
    if(cur_k == 0): #먹거나 먹지 X
        f(idx+1, e, cur_k+arr[idx]) #먹음
        f(idx+1, e, cur_k) # 먹지않음
        
f(0, 0, 0)
print(max_e)