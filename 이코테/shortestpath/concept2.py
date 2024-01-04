# 다익스트라 소스코드2 : 어려운데 빠른
#                       노드 개수가 10,000개가 넘어간다면 개선된 다익스트라 알고리즘 사용하슈
#                       시간복잡도 O(ElogV) 보장 => v는 노드개수, e는 간선
#                       => 힙 자료구조 이용

# 힙: 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나(우선순위 높은데이터 먼저 삭제) => 리스트보다 힙이 더 빠름
#     PriorityQueue heapq 둘다 가능하지만 heapq가 더 빠르니까 이거 쓰슈
#     (가치,무게)를 넣게 된다면 첫번째 원소를 우선순위로 보고 최소 힙은 최소값을, 최대 힙은 최대값 먼저 꺼낸다.
#      => 파이선라이브러리는 최소힙이 기본이다.
#      => 최대힙을 사용하고 싶으면 넣을때 - 붙이고 빼고 -다시 붙여주자(자주쓰임)  

import heapq
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

def dijkstra(start):
    q =[]
    heapq.heappush(q(0,start))
    distance[start] = 0
    while q:
        dist,now =heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost <distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
    # 모든 노드로 가기 위한 최단 노드 출력 
for i in range(1,n+1):
    if distance[i] == INF:
        print('도달할 수 없슈')
    else:
            print(distance[i])