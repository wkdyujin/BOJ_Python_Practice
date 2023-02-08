n, k = map(int, input().split())

res = 0 # 약수
num = 0 # 약수 개수

for i in range(1, n + 1):
    if(n % i == 0):
        num += 1
        res = i
    if(num == k): # k번째 약수 발견 시 반복문 탈출
        break

if(num < k):
    print(0)
else:
    print(res)