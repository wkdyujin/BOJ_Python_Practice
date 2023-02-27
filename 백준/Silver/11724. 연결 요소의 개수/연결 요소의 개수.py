from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

q = deque([])
visited = []
res = 0

def bfs(v):
    q.append(v)
    while(q):
        node = q.popleft()
        if(node not in visited):
            q.extend(graph[node])
            visited.append(node)
    visited.append(v)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)
    
for i in range(n):
    if(i not in visited):
        bfs(i)
        res += 1
    
print(res)