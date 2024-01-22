import sys

input = sys.stdin.readline

n = int(input())

arr = [[0, 0] for _ in range(n)]
for i in range(n):
    arr[i][0], arr[i][1] = map(int, input().split())

arr.sort(key=lambda x: (x[1], x[0]))  # 종료 시간을 우선으로 모든 인덱스를 오름차순 정렬

count = 1  # 첫번째 회의는 무조건 사용 가능
end = arr[0][1]  # 첫번째 회의의 종료 시간

for i in range(1, n):  # 종료 시간이 이른 순서대로 회의실 배정
    if arr[i][0] >= end:  # 시작 시간이 이전 회의 종료 시간보다 늦으면 배정
        end = arr[i][1]
        count += 1

print(count)
