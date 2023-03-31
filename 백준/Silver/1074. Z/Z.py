N, r, c = map(int, input().split())

res = 0 # 방문 위치

while N > 0:
    N -= 1
    w = 2 ** N
    
    if(r < w and c < w): # 1사분면
        res += 0
        
    elif(r < w and c >= w): # 2사분면
        res += w * w
        c -= w   
        
    elif(r >= w and c < w): # 3사분면
        res += w * w * 2
        r -= w

    else: # 4사분면
        res += w * w * 3
        c -= w
        r -= w
        
print(res)