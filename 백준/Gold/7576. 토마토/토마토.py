import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = set()
q = deque([])

for i in range(N):
    for j in range(M):
        if(graph[i][j] == 1):
            q.append((i, j)) # 익은 토마토 좌표
            visited.add((i, j))

fx = [1, -1, 0, 0]
fy = [0, 0, 1, -1]

def bfs():
    day, today = 0, 0
    iterator = len(q) # 하루에 반복해야하는 횟수
    
    while q:
        x, y = q.popleft()
        today += 1 # 오늘 익은 토마토 수
        
        for i in range(4):
            dx = x + fx[i]
            dy = y + fy[i]

            if(0 <= dx < N and 0 <= dy < M and graph[dx][dy] == 0 and (dx, dy) not in visited):
                q.append((dx, dy))
                visited.add((dx, dy))
                graph[dx][dy] = 1
        
        if(iterator == today):
            day += 1
#             for i in graph:
#                 print(i)
#             print(day, end = '\n\n')
            today = 0
            iterator = len(q)
        
    for line in graph:
        if(0 in set(line)):
            return -1 # 안 익은 토마토가 있을 때
        
    return day - 1 # 마지막 pop 세지 않음

print(bfs())