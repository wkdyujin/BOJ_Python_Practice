N, M = map(int ,input().split())
r,c,view = map(int, input().split())
arr = []
for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

# 북 동 남 서
fx = [-1,0,1,0]
fy = [0,1,0,-1]

def isClean(x, y):
    for i in range(4):
        dx = x + fx[i]
        dy = y + fy[i]
        if(arr[dx][dy] == 0):
            return False
    return True

def f(x, y, cur_v):
    if(arr[x][y] == 0):
        arr[x][y] = 2
        
    if isClean(x, y): # 주위에 0이 없다
        dx = x + fx[(cur_v + 2) % 4]
        dy = y + fy[(cur_v + 2) % 4]
        if(arr[dx][dy] != 1): # 벽이 아니면 후진 가능
            f(dx, dy, cur_v) # 후진
            
    else: # 주위에 0이 있다 -> 회전
        new_v = (cur_v + 3) % 4
        dx = x + fx[new_v]
        dy = y + fy[new_v]
        if(arr[dx][dy] == 0):
            f(dx, dy, new_v) # 한 칸 전진
        else:
            f(x, y, new_v) # 방향만 변경
            
f(r, c, view)

res = 0
for line in arr:
    res += line.count(2)
print(res)