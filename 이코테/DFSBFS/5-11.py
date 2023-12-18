# 문제: 미로를 탈출하기 위해 움직여야하는 최소한의 칸 수?
#       동빈이는 1,1에 있고 출구는n,m 
#       괴물은 0에 있고 없는 부분은 1 반드시 탈출할수 있는 형태 
# 방법: 시작지점부터 가장 가까운 노드부터 차례로 탐색하는 BFS 이용 
#       0,0 -> n-1,m-1 으로 이동해야하므로 큐에 첫 노드를 넣고, 빼고 주변을 탐색(방향을 미리 지정했음)후 
#       갈수있는 노드(1)라면 이동후 +1해준다.(그래서 이미 이동한 노드는 1에서 더해진값이된다.)
#       
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph(list(map(int,input())))

dx =[-1,1,0,0] 
dy =[0,0,-1,1]

from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:# 큐가 빌때까지
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx >=n or ny<0 or ny>=n: # 범위 벗어나면 무시
                continue
            if graph[nx][ny]==0: # 벽인경우 무시
                continue
            if graph[nx][ny] == 1:# 처음 방문하는 경우에만 최단거리 기록 
                graph[nx][ny] = graph[x][y] + 1 #기존 값에 1씩더해서 거리 측정
                queue.append((nx,ny))
    return graph[n-1][m-1] #최종도착노드에 저장된 최단거리 리턴 

print(bfs(0,0))# 동빈의 위치 1,1의미(graph는 0,0부터 시작)