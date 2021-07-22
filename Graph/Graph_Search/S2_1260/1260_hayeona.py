import sys
from collections import defaultdict
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = defaultdict(list)
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for key,value in graph.items():
    value.sort()

def dfs(start):
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node,end= ' ')
            visited.append(node)
            stack.extend(graph[node][::-1])

def bfs(start):
    que = [start]
    visited = []
    while que:
        node = que.pop(0)
        if node not in visited:
            print(node,end =' ')
            visited.append(node)
            for x in graph[node]:
                if x not in visited:
                    que.append(x)
dfs(v)
print()
bfs(v)
