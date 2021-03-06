from collections import deque

def bfs(graph,start,visited):
    
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()

        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




def dfs(graph,v,start):
    
    visited[v] = True
    print(v, end =" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph =  [

    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9