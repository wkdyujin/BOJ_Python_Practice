from collections import deque
N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input())))

q = deque([(0,0)]) # x, y, 거리
fx = [0, 0, 1, -1]
fy = [1, -1, 0, 0]

while(q):
    x, y = q.popleft()
    
    for i in range(4):
        dx = x+fx[i]
        dy = y+fy[i]
        
        if(0 <= dx < N and 0 <= dy < M and arr[dx][dy] == 1):
                q.append((dx,dy))
                arr[dx][dy] = arr[x][y] + 1
                
print(arr[N-1][M-1])