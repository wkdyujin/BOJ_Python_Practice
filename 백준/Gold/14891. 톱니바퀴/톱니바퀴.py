arr = []
for i in range(4):
    arr.append(input())

near = [[[1, 6]], [[0,2], [2,6]], [[1,2], [3,6]], [[2, 2]]] # 근처 톱니 번호

K = int(input())

for i in range(K): # 전체를 K번 회전
    stack = [] # 회전할 톱니 바퀴 탐색에 사용
    visited = set()
    rotate = [] # 회전할 때 사용
    
    n, r = map(int, input().split())
    n -= 1
    stack.append((n, r))
    
    while(stack):
        cur_b, cur_r = stack.pop()
        rotate.append((cur_b, cur_r))
        visited.add(cur_b)
        
        cur_idx= 0
        for near_bike in near[cur_b]: # 주위 톱니 확인
            if(near_bike[0] not in visited):
                if (near_bike[1] == 6):
                    cur_idx = 2
                else:
                    cur_idx = 6

                if(arr[near_bike[0]][near_bike[1]] != arr[cur_b][cur_idx]): # 다르면 주위 톱니도 회전
                        stack.append((near_bike[0], cur_r * (-1)))         
    
    # 회전
    for n, r in rotate:
        if r == 1: # 시계 방향 회전
            arr[n] = arr[n][-1] + arr[n][:-1] # 마지막 요소를 맨 앞에
        else:
            arr[n] = arr[n][1:] + arr[n][0] # 맨 앞 요소를 마지막에
    
res = 0
for i in range(4):
    if(int(arr[i][0]) == 1):
        res += 2**i
print(res)