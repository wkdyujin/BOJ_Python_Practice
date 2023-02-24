def solution(brown, yellow):
    answer = []
    
    w = 3
    while(True):
        h = (brown - w*2)//2 + 2
        if(w*h == brown+yellow):
            answer = [w, h]
            break
        else:
            w += 1
            
    answer.sort(reverse = True)
    return answer