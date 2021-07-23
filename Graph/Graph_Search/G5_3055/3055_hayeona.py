from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
water = []
for i in range(n):
    temp = list(map(str,input().strip()))
    for j in range(m):
        if temp[j] == '*':
            water.append([i,j])
        elif temp[j] == 'S':
            start = [(i,j)]
        elif temp[j] == 'D':
            end = [(i,j)]
    graph.append(temp)

dx,dy = [0,1,0,-1],[1,0,-1,0]
count = 0

def bfs(arr,flag):
    que = deque(arr)
    candidate = []
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<= nx < n and 0<=ny<m:
                if not flag:
                    if (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                        graph[nx][ny] = '*'
                        candidate.append((nx,ny))
                else:
                    if graph[nx][ny] == 'D': return True
                    if graph[nx][ny] == '.' and graph[x][y] == 'S':
                        graph[nx][ny] = 'S'
                        candidate.append((nx,ny))
    return candidate


while True:
    start = bfs(start, True)
    water = bfs(water,False)
    count += 1

    if start == True:
        print(count)
        break

    if len(start) == 0:
        print("KAKTUS")
        break

    temp = []
    for i,j in start:
        if graph[i][j] == 'S':
            temp.append((i,j))
    start = temp