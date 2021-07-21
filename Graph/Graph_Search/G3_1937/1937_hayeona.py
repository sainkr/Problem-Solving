import sys
input = sys.stdin.readline

dx,dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y):
    if dp[x][y] > 1:
        return dp[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
dp = [[1] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)