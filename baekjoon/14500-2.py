# max_value값을 max로 수시로 비교하는게 아니라 아예set()에 모두 넣어 max구하기(list보다 빠르다.)
import sys

input = sys.stdin.readline # 더 빨리 입력 받기 

n,m = map(int,input().split())
array = [list(map(int,input().rsplit())) for _ in range(n)] #.rstrip() :문자열 끝의 '\n' 제거
direction = [(1,0),(-1,0),(0,-1),(0,1)] # 상하좌우
visited = [[False]*m for _ in range(n)] # 방문확인
max_value = set() 

def dfs(x,y,step,total): # ㅗ모양을 제외한 나머지는 dfs통해 모두 나올수 있는 모양임(4번 진행시)
    if step == 4: 
        max_value.add(total) #set()에 넣기
        return # 함수에 if문 있을때는 return(=>함수를 나오기), 반복문에 if문 있을때는 break(=>if문을 나오기)
    for i in range(4):
        dx = x+direction[i][0]
        dy = y+direction[i][1]
        if 0<=dx<n and 0<=dy<m and not visited[dx][dy]:
            visited[dx][dy] = True
            dfs(dx,dy,step+1,total+array[dx][dy])
            visited[dx][dy] = False 
            
def excecption(x,y): # ㅗ모양일때는 dfs 불가능함 1 2 3 라면 2에서 탐색할때 3과4를 동시에 진행못함
                     #                            4
                     # 사방탐색을 진행해서 범위를 벗어나지않는다면 리스트에 원소로 담고 
                     # 원소가 4개가 담긴다면 가장 최소값은 제외,3개가 담긴다면 다 더하고, 2개 이하면 0.
    array2 = []
    for i in range(4):
        dx = x+direction[i][0]
        dy = y+direction[i][1]
        if 0<=dx<n and 0<=dy<m: #어짜피 사방탐색가능한것만 볼꺼니까 방문여부는 필요없지 않을까?
            array2.append(array[dx][dy])
    if len(array2) == 4:
        max_value.add(array[x][y]+sum(array2)-min(array2)) #set()에 넣기
        return
    elif len(array2) == 3:
        max_value.add(array[x][y]+sum(array2)) #set()에 넣기
        return 
for i in range(n):
    for j in range(m):
        visited[i][j] = True # 시작점 방문 표시
        dfs(i,j,1,array[i][j])
        visited[i][j] = False
        excecption(i,j)
print(max(max_value)) #set()의 최고값 꺼내기