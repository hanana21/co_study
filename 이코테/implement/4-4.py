# 문제 : 캐릭터가 방문한 칸의 갯수를 구하라 
#        1. 현재 위치, 방향을 기준으로 왼쪽방향 부터 
#        2. 왼쪽 방향에 가보지 않은 칸이 있다면 왼쪽 회전후 한칸 전진, 아니라면 왼쪽 회전만하고 1단계로
#        3. 네방향 모두 가본 칸이거나 바다면 방향 유지한채 한칸 뒤로가고 1단계로 돌아간다.
#           이때, 뒤가 바다라서 뒤로 못간다면 움직임을 멈춘다.
#        4. 육지 = 0, 바다 =1 외각은 항상 바다이고, 육지로만 이동가능함
# 푸는 방법: 1. 왼쪽 회전 함수 만들기
#            2. 방문 기록을 남기기 위한 2차원 리스트 만들기 
#            3. 조건에 따라 시뮬레이션 
n,m = map(int,input().split())
x,y,direction = map(int,input().split())
#전체 맵의 정보 받기: 리스트 컴프리헨션 2차원 리스트 선언시 효율적
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
#방문 기록:n x m
d = [[0]*m for _ in range(n)]
d[x][y]=1 #지금위치 방문 표시
# 방향 설정: 한칸 전진시 이용(북,동,남,서)=> 방향을 미리 설정해주면 좋음
dx = [-1,0,1,0]
dy = [0,1,0,-1]
#왼쪽으로 회전(기능 분리) 
def turn_left():
    global direction # 밖에서 선언된 전역변수라서
    direction -= 1
    if direction == -1:
        direction = 3
count = 1 #지금 위치 포함
turn_time = 0
while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]
    if array[nx][ny] == 0 and d[nx][ny] == 0: # 가본적 없고, 육지라면
        d[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue # 없어도 되는데 왜한거지? 시간 단축하려고 그러나?
    else:
        turn_time +=1 #이 방향은 갈곳 없어서 회전한번 했다는 뜻(4번하면 모든곳 갈곳없슈의미)
                      # 여기에 continue를 쓰면 turn_time이 4가 되더라도  if turn_time == 4: 실행이 안되니 무한루프
    if turn_time == 4: # 사방이 바다 혹은 한번 갔던곳이라면
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:# 만약 한칸 뒤가 육지라면 이동
            x = nx
            y = ny
        else: # 바다로 막혀있다면 끝
            break
        turn_time = 0     
print(count)





                                    