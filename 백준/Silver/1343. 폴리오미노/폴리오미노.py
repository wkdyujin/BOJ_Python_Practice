board = input() # XX.XXXX
arr = []
arr = board.split(".")

res = ''
f = 0
for i in range(len(arr)):
    cnt = arr[i].count('X')
    if(cnt % 4 == 0): # 4로 나누어 떨어질 때 (4,8,12...)
        res += 'AAAA' * (cnt//4)
    elif(cnt % 2 == 0): # 4로 나누어 떨어지지 않고 2로 나누어 떨어질 때(2,6...)
        if(cnt == 2):
            res += 'BB'
        else:
            res += 'AAAA' * (cnt//4) + 'BB'
    else:
        f = -1
        break
    res += '.'
    
if(f == 0):
    print(res[:-1])
else:
    print(f)