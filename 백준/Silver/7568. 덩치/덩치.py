n = int(input())
weights = []
heights = []
for _ in range(n):
    weight, height = map(int, input().split())
    weights.append(weight)
    heights.append(height)

ranks = [1 for _ in range(n)] # [1, 1, 1, 1, 1]

for i in range(n):
    for j in range(n):
        tie = 0 # rank가 같은 사람들 수
        if(i != j):
            if(weights[i] < weights[j] and heights[i] < heights[j]):
                ranks[i] += tie + 1
            elif(weights[i] > weights[j] and heights[i] > heights[j]):
                continue
            else:
                tie += 1

for rank in ranks:
    print(rank, end = " ")