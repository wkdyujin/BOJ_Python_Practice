n = int(input())
numList = list(map(int, input().split()))
m = int(input())
targetList = list(map(int, input().split()))

numList.sort()

# 배열을 넘길까, for문으로 하나만 넘길까 고민
def f(low, high, target):
    mid = (low + high) // 2
    # print("타겟{3}일때, low:{0}, mid:{1}, high:{2}".format(low, mid, high, target))
    
    # 정수를 찾았을 경우
    if(numList[mid] == target):
        return 1
    
    # 찾지 못했을 경우
    else:
        if(numList[mid] > target): # target이 mid보다 작을 때
            if(low == mid):
                return 0
            return f(low, mid - 1, target)
        else: # target이 mid보다 클 때
            if(high == mid):
                return 0
            return f(mid + 1, high, target)
    
       
for target in targetList: # 1 3 7 9 5
    print(f(0, n-1, target))