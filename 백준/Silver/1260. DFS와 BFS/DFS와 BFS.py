from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for nodes in graph:
    nodes.sort()

def dfs(V):
    visited = set()
    stack = [V]
    while stack:
        cur = stack.pop()
        if cur not in visited:
            print(cur, end = ' ')
            visited.add(cur)
            for i in range(len(graph[cur])-1, -1, -1):
                stack.append(graph[cur][i])

def bfs(V):
    visited = set()
    queue = deque([V])
    while(queue):
        cur = queue.popleft()
        if cur not in visited:
            print(cur, end = ' ')
            visited.add(cur)
            queue.extend(graph[cur])
        

dfs(V)
print()
bfs(V)