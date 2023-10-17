def solution(n):
    # 재귀도 아니고 그냥 반복문이다?
    ans = 1
    
    while(n > 2):
        if n%2==0:
            n = n//2
        else:
            n = n-1
            ans += 1
    
    return ans