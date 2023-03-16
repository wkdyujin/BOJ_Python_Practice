from collections import deque

def bfs():
    q = deque([(0,0)])
    
    while(q):
        x, y = q.popleft()
        score = arr[x][y]
        
        if(score == -1):
            return "HaruHaru"
        
        if(score != 0):
            if(x + score < n): # 0+1 < 3
                q.append((x + score, y))
            if(y + score < n): # 0+1 < 3
                q.append((x, y + score))
    
    return "Hing"
    
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print(bfs())