def solution(s):
    answer = 0
    x = s[0]
    x_cnt, nx_cnt = 1, 0
    
    if(len(s) == 1): # 문자열이 한글자일 때
        answer += 1
    
    for i in range(1, len(s)):
        if(i == len(s) - 1 and x_cnt != nx_cnt): # 남은 부분이 있을 때
            answer += 1
            break
            
        if(x_cnt == 0): # x가 정해져있지 않을 때
            x = s[i]
            x_cnt += 1
            if(i == len(s) - 1 and x_cnt != nx_cnt):
                answer += 1
            continue
            
        if(x == s[i]):
            x_cnt += 1
        else:
            nx_cnt += 1
            
        if(x_cnt == nx_cnt):
            answer += 1
            x_cnt, nx_cnt = 0, 0 # 초기화
        
    return answer