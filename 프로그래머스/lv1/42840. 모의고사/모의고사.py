def solution(answers):
    answer = []
    
    p_list = [0, 0, 0]
    p1_list = [5, 1, 2, 3, 4]
    p2_list = [2, 1, 2, 3, 2, 4, 2, 5]
    p3_list = [5, 3, 3, 1, 1, 2, 2, 4, 4, 5]
    
    for i in range(len(answers)): # 5
        # 1번
        if(answers[i] == p1_list[(i+1)%5]):
            p_list[0] += 1
        
        # 2번
        if(i % 2 == 0): # 짝수일 때 무조건 2
            if(answers[i] == 2):
                p_list[1] += 1
        else: # 홀수일 때
            if(answers[i] == p2_list[i%8]):
                p_list[1] += 1
                
        # 3번
        if(answers[i] == p3_list[(i+1) % 10]):
            p_list[2] += 1
    
    m = max(p_list)
    for i in range(1, len(p_list)+1):
        if(p_list[i-1] == m):
            answer.append(i)
            
    return answer