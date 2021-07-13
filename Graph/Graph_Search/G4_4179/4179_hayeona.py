import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
fire = []
answer = 0
dx,dy = [0,1,0,-1], [1,0,-1,0]

#input 처리
for i in range(n):
    temp = list(map(str,input().strip()))
    for j in range(m):
        if temp[j] == 'J':
            start = [(i,j)]
        elif temp[j] == 'F':
            fire.append((i,j))
    graph.append(temp)


def bfs(arr, flag):
    que = deque(arr)
    result = []
    while que:
        x,y = que.popleft()
        if flag: # 종료 조건 탐색 (미로의 가장자리이면서, 지나갈 수 있다면)
            if (x == 0 or x == n - 1 or y == 0 or y == m - 1) and graph[x][y] == 'J':
                return True

        for i in range(4): # 상하좌우로 BFS 탐색 및 업데이트 진행
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'J')and graph[x][y] == 'F': # 불이 상위조건이므로, 불부터 탐색
                    graph[nx][ny] = 'F'
                    result.append((nx,ny))
                elif graph[x][y] == 'J' and graph[nx][ny] == '.':
                    graph[nx][ny] = 'J'
                    result.append((nx, ny))
    return result


while True:
    start = bfs(start,True)
    fire = bfs(fire,False)
    answer += 1

    if start:
        print(answer)
        break
    if len(start) == 0:
        print('IMPOSSIBLE')
        break
    temp = []
    for i,j in start:
        if graph[i][j] == 'J':
            temp.append((i,j))
    start = temp

