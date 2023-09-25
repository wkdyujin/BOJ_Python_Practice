import copy

N, M = map(int, input().split())
arr = []
xy = []
max_safe = 0

for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

for i in range(N):
    for j in range(M):
        if(arr[i][j] == 0):
            xy.append((i, j))


fx = [0, 0, -1, 1]
fy = [-1, 1, 0, 0]

def dfs(graph):
    stack = []
    visited = []
    for i in range(N):
        for j in range(M):
            if(graph[i][j] == 2):
                stack.append((i,j))
                visited.append((i,j))
                
    while(stack):
        x, y = stack.pop()
        for k in range(4):
            dx = x + fx[k]
            dy = y + fy[k]
            
            if(0 <= dx < N and 0 <= dy < M and graph[dx][dy] == 0 and (dx, dy) not in visited):
                graph[dx][dy] = 2
                stack.append((dx, dy))
                visited.append((dx, dy))
        
    return graph

graph = copy.deepcopy(arr)

for i in range(len(xy)):
    x1, y1 = xy[i]
    graph[x1][y1] = 1
    
    for j in range(i+1, len(xy)):
        x2, y2 = xy[j]
        if(graph[x2][y2] == 0):
            graph[x2][y2] = 1
            
            for k in range(j+1, len(xy)):
                x3, y3 = xy[k]
                if(graph[x3][y3] == 0):
                    graph[x3][y3] = 1

                    # 바이러스 전파
                    graph2 = copy.deepcopy(graph)
                    cur_safe = 0
                    for line in dfs(graph2):
                        cur_safe += line.count(0)
                    max_safe = max(max_safe, cur_safe)
            
                    graph[x3][y3] = 0
        
            graph[x2][y2] = 0
    
    graph[x1][y1] = 0
                
print(max_safe)