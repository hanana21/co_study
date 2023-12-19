from collections import deque
# 다시 풀어보기 
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
#방향지정하기
dx =[-1,1,0,0]
dy =[0,0,-1,1]
# 큐 사용
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue: #큐가 빌때 까지
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어나면 무시
            if nx <0 or ny <0 or nx >=n or ny >=m:
                continue
            # 벽을 만나면 무시
            if graph[nx][ny]==0:
                continue
            # 가본적 없는 노드면 최단거리 기록 
            if graph[nx][ny]==1: #첫번째 시작위치로 갈수도 있지만 이문제는 단순히 가장 오른쪽아래로 이동하기 때문에 괜츈
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))



