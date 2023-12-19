# BFS : 너비 우선 탐색=> 가까운 노드부터 탐색 
#       큐를 이용 
# 사용 방법: 1노드를 큐에 넣고, 방문처리 => 1을 꺼내고 인접노드들을 큐에 넣고(작은수 부터) 방문처리
#            그다음 노드를 꺼내고 그 노드의 인접 노드 넣기(인접노드 없으면 넣는거 무시)
#            모든 노드를 차례대로 꺼내면 끝 
# DFS보다 실제 수행 시간이 좋은 편
# 최단거리 문제에 활용(가장 가까운노드부터 탐색) 

from collections import deque

#BFS 메소드 정의 
def bfs(graph,start,visited):
    visited[start] = True #방문 처리
    queue =deque([start]) 
    while queue: #큐가 빌때까지 반복 
        v = queue.popleft()#빼고
        print(v,end=' ') 
        # 해당 원소에 연결된 노드(아직 방문안한) 큐에 넣기 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True #방문처리

# 각 노드에 연결된 정보 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8], #1노드에 연결된 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9
bfs(graph,1,visited) 
