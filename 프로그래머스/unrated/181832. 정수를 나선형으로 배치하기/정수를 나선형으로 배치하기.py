def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    print(answer)
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, w, n = 0, 0, n-1, 1
    
    while(w > 0):
        for i in range(4):
            for _ in range(w):
                answer[x][y] = n
                n += 1
                x += dx[i]
                y += dy[i]
        x += 1
        y += 1
        w -= 2
        
    if(w == 0):
        answer[x][y] = n
    
    
    return answer