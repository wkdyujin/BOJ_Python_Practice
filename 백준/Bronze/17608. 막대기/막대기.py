import sys

sticks = []
n = int(input())

sticks.append(int(input())) # 첫번째 막대

for i in range(n - 1):
    curStick = int(sys.stdin.readline())
    while(sticks[-1] <= curStick): # 마지막 막대가 새 막대보다 짧거나 같을 때
        sticks.pop() # 마지막 막대 제거
        if(len(sticks) == 0):
            break
    sticks.append(curStick)
    
print(len(sticks))