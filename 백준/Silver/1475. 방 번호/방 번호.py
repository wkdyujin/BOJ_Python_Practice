roomNum = input()
numCnt = [0] * 9

for n in range(len(roomNum)):
    if (int(roomNum[n]) == 9):
        numCnt[6] += 1
    else:
        numCnt[int(roomNum[n])] += 1
        
numCnt[6] = (numCnt[6] + 1) // 2

print(max(numCnt))