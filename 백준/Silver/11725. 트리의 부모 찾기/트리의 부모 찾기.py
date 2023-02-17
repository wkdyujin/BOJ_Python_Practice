import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
queue = deque([1])
parent = [1, 1] + [0] * (n - 1)

while(len(queue) > 0):
    pop = queue.popleft() # 1
    
    for i in range(len(graph[pop])): # graph[pop][i] => 6, 4
        if(parent[graph[pop][i]] == 0): # 부모 없을 시
            parent[graph[pop][i]] = pop # 부모 넣어줌
            queue.append(graph[pop][i])
        
for i in parent[2:]:
    print(i)