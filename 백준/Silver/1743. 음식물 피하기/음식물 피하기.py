from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())
graph = [[False for _ in range(m)] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = True # 음식물

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    cnt = 1
    
    while(q):
        x, y = q.popleft()
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
                
            # 좌표가 범위 내에 존재 & 해당 좌표값이 1일 경우
            if(0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]):
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt

max_cnt = 0 # 제일 큰 음식물의 크기

for i in range(n):
    for j in range(m):
        if(graph[i][j] and not visited[i][j]):
            max_cnt = max(bfs(i, j), max_cnt)

print(max_cnt)