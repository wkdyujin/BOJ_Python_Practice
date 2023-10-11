import sys
input = sys.stdin.readline

N, M, A, B, C = map(int , input().split())
graph = [[] for _ in range(N+1)]
max_list = []
visited = set()

for i in range(M):
    n1, n2, c = map(int, input().split())
    graph[n1].append((n2, c))
    graph[n2].append((n1, c))


def dfs(n, total_c, max_c):
    visited.add(n)
    
    if(n == B): # 최종 목적지 도착
        if(total_c > C): # 예산 초과
            return
        max_list.append(max_c)
        return
    
    for (node, cost) in graph[n]:
        if(node not in visited):
            dfs(node, total_c+cost, max(max_c, cost))
            visited.remove(node)
            
dfs(A, 0, 0)

if(len(max_list) > 0):
    print(min(max_list))
else:
    print(-1)