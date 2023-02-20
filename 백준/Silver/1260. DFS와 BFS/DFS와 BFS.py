from collections import deque

visited_dfs = []
visited_bfs = []

def dfs(v):
    visited_dfs.append(v)
    for i in graph[v]:
        if(i not in visited_dfs):
            dfs(i)       
    return visited_dfs

def bfs(v):
    q = deque([v])
    while q:
        node = q.popleft()
        if(node not in visited_bfs):
            visited_bfs.append(node)
            q.extend(graph[node])
    return visited_bfs


n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]

for _ in range(m):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
    
for i in graph:
    i.sort()
    
print(*dfs(v))
print(*bfs(v))