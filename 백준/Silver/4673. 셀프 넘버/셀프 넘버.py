arr = []
num = 1
while(num < 10000): # 100보다 작은 d(n) 전부 구하기
    res = num
    for i in str(num):
        res += int(i)
    arr.append(res)
    num += 1

for i in range(1, 10000 + 1):
    if(i not in arr):
        print(i)