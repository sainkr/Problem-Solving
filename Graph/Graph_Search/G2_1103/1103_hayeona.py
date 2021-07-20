import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
flag = False
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

cc = 0
def dfs(x, y):
    global flag
    # 종료 조건1: 범위를 벗어났거나, 구멍에 빠졌다면
    if not (0 <= x < n and 0 <= y < m) or arr[x][y] == 'H': return 0

    # 종료 조건2: 이미 탐색한 곳이라면
    if visited[x][y]:
        flag = True
        return -1

    # 종료 조건3: 해당 지역에 대한 업데이트가 끝났다면,
    if dp[x][y] != -1: return dp[x][y]


    visited[x][y] = True
    count = int(arr[x][y])
    for i in range(4):
        dp[x][y] = max(dp[x][y], dfs(x + dx[i] * count, y + dy[i] * count) + 1)
        if flag:
            return -1
    visited[x][y] = False
    return dp[x][y]


print(dfs(0, 0))
