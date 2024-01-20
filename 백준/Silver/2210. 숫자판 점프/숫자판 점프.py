import sys
limit_number = 1024*25
sys.setrecursionlimit(limit_number)

graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

fx = [0, 0, -1, 1]
fy = [1, -1, 0, 0]
nums = set()

def dfs(x, y, s):
    if len(s) == 6:
        nums.add(s)
        return

    for i in range(4):
        dx = x + fx[i]
        dy = y + fy[i]
        
        if 0 <= dx < 5 and 0 <= dy < 5:
            dfs(dx, dy, s + str(graph[dx][dy]))
    
            
for x in range(5):
    for y in range(5):
        dfs(x, y, str(graph[x][y]))

print(len(nums))