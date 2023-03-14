from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

# 탐색할 x, y좌표 (상하좌우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]                
                
def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0 # 방문 처리
    
    while(q):
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if(nx < 0 or nx >= m or ny < 0 or ny >= n):
                continue
                
            if(graph[nx][ny] == 1):
                q.append((nx, ny))
                graph[nx][ny] = 0

# 각 테스트 케이스에 대하여             
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    res = 0
    
    # 그래프 생성
    for _ in range(k):
        x, y = map(int,input().split())
        graph[x][y] = 1
    
    # 탐색
    for i in range(m):
        for j in range(n):
            if(graph[i][j] == 1):
                bfs(i, j)
                res += 1
                
    print(res)