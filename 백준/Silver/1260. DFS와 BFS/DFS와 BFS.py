# 답
from collections import deque

def dfs(v):
    visited = []
    stack = [v]
    
    for i in range(1, n + 1): # graph 정렬
        graph[i].sort(reverse = True)
    
    while(stack):
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node]) # extend: 리스트 끝에 가장 바깥쪽 iterable의 모든 항목 삽입
    return visited


def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    
    for i in range(1, n + 1): # graph 정렬
        graph[i].sort()
    
    while(queue):
        node = queue.popleft()
        if(not visited[node]):
            print(node, end = ' ')
            visited[node] = True
            for i in graph[node]:
                queue.append(i)
                
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1) ]

for i in range(1, m + 1):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
    
print(*dfs(v))
bfs(v)