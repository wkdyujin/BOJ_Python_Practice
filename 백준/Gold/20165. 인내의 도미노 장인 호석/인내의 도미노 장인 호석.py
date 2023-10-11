N, M, R =map(int,input().split())
matrix = [] # 높이 표현 매트릭스
res_m = [['S' for _ in range(M)] for _ in range(N)] # 쓰러짐 표현 매트릭스(결과)

for _ in range(N):
    matrix.append(list(map(int, input().split())))

score = 0
fx = [0, 0, 1, -1]
fy = [1, -1, 0, 0]
dic = dict({'E':0,'W':1,'S':2,'N':3})

def fight(x1, y1, d, x2, y2):
    # 공격
    s = [(x1, y1)]
    score = set() # 쓰러뜨린 도미노 좌표
    
    while(s):
        x, y = s.pop()
        it = matrix[x][y] # 반복 횟수
        for _ in range(it): 
            if(0 <= x < N and 0 <= y < M):
                if(res_m[x][y] == 'S'):
                    res_m[x][y] = 'F'
                    s.append((x, y)) # 연쇄적으로 쓰러뜨림
                    score.add((x,y))
                x += fx[dic[d]]
                y += fy[dic[d]]
    # 수비
    if(res_m[x2][y2] == 'F'): # 쓰러져있다면
        res_m[x2][y2] = 'S' # 다시 세우기
        
    return len(score)

def check():
    for line in res_m:
        print(line)

for _ in range(R):
    X1, Y1, D = input().split()
    X2, Y2 = map(int, input().split())
    score += fight(int(X1)-1, int(Y1)-1, D, X2-1, Y2-1)
    
print(score)
for line in res_m:
    print(*line)