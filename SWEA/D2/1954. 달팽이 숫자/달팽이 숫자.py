T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    print("#" + str(test_case))
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    x, y = 0, 0
    n, side = 1, N - 1
    while side > 0:
        for i in range(4):
            for _ in range(side):
                arr[x][y] = n
                n += 1
                x += dx[i]
                y += dy[i]
        x += 1
        y += 1
        side -= 2

    if side == 0:
        arr[x][y] = n

    for line in arr:
        print(*line)