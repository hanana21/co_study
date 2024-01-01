# 최단 경로: 가장 짧은 경로 찾는 알고리즘
#            각 상황에 맞은 효율적인 알고리즘이 정립 되어있음
#            보통 코테는 단순히 최단거리를 출력하는 문제가 많이 출제 
#            그리디, 다이나믹의 한 유형으로 볼 수 있음

# 종류: 다익스트라, 플로이워셜(2개가 자주 나옴),벨만포드(이거는 안다룰거임) 
# 1. 다익스트라 
#    : 특정노드에서 다른 노드까지의 최단거리를 각각 구해주는 알고리즘 
#      - 음의 간선이 없을 때 정상적으로 작동(실제 길도 그렇쥬)
#      - 가장 비용이 적은 노드를 선택하기 때문에 그리디 알고리즘으로 분류된다.
#      - 각 노드에 대한 현재까지의 최단거리 정보를 1차원 리스트(최단거리 테이블)에 저장하여 갱신한다.
#      - 무조건 2가지 방법 외울것!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
#      - 방법:
#           1) 최단거리 테이블을 INF로 초기화
#           2) 기준 노드에서 연결된 노드의 간선을 최단거리 테이블에 입력
#           3) 최단거리가 작은것 부터 탐색(같다면 작은 수의 노드부터)
#           4) (새노드 ~인접노드) + (기준노드~새노드)의 값을 기존에 저장된 값과 비교하여 최소값을 갱신, 새노드는 방문처리
#           5) 이때 한단계에서 선택된 새노드는 무조건 최소값이다=> 한단계에 최소한 하나는 최소값 확정된다.
#                                                             => 마지막노드는 굳이 확인 할 필요없다.
# 소스코드1(구현하기 쉽지만 느림) : 시간 복잡도 O(V2)=> v는 노드갯수
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) # 노드, 간선
start = int(input()) # 시작점
graph = [[] for i in range(n+1)] # 정보저장: n까지라서 n+1
visited =[False] * (n+1) # 방문 확인용
distance = [INF] * (n+1) # 최단거리 저장용

# 모든 간선 정보 받기 
for i in range(m):
    a,b,c = map(int,input().split()) # a->b 비용 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드의 번호 반환하는 함수
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 함수
def dijkstra(start):
    distance[start] = 0 # 시작노드는 최단거리 0
    visited[start] = True
    for j in graph[start]: # 시작노드의 인접노드에 대해 최단거리 갱신
        distance[j[0]] = j[1] # graph[0] = 도착노드, graph[1] = 간선 
    # 시작 노드를 제외한 n-1노드에 대해 반복 
    for i in range(n-1):
        now = get_smallest_node() # 최단 거리 가장 짧은 노드 꺼내기 
        visited[now] = True # 방문처리 
        for j in graph[now]:
            distance[j[0]] = min(distance[j[0]],distance[now]+j[1]) # 저장된 최단거리 vs start->now->도착점 
    
dijkstra(start)

    # 모든 노드로 가기 위한 최단 노드 출력 
for i in range(1,n+1):
    if distance[i] == INF:
        print('도달할 수 없슈')
    else:
            print(distance[i])