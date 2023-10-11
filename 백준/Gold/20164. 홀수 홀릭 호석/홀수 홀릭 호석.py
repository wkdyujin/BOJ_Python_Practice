N = int(input())
minn, maxn = 1e9, 0 
def f(n, cnt):
    for c in str(n):
        if(int(c) % 2 != 0): # 홀수
            cnt += 1
            
    if(len(str(n)) == 1): # 한자릿수
        global minn, maxn
        minn = min(minn, cnt)
        maxn = max(maxn, cnt)
        return # 재귀 종료
    
    elif(len(str(n)) == 2): # 두자릿수
        f(int(str(n)[0]) + int(str(n)[1]), cnt)
        
    else: # 세자릿수 이상
        for i in range(1, len(str(n)) + 1):
            for j in range(i+1, len(str(n))):
                f(int(str(n)[:i]) + int(str(n)[i:j]) + int(str(n)[j:]), cnt)

f(N, 0)
print(minn, maxn)