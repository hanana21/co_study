# 문제:  N x N 정사각형 공간에서 (1,1)에 있는 여행가가 입력받은 값에 따라 도착하는 좌표는?
#        (L,R,U,D만 입력가능, 단 공간을 벗어나는 경우면 이동안함)
# 풀이: 시뮬레이션 문제
#       1. 방향을 정의해준다.
#          => 입력받을 l,r,u,d와 비교할 l,r,u,d를 요소로 가지는 리스트를 만들고 
#             이 순서에 맞게 이동시 변화될 dx,dy의 값을 지정해준다.
#       2. 입력받은 방향의 갯수만큼 이동을 진행 + 입력받은 문자와 이동방향을 매칭 시켜야한다.
#           => 입력받은 갯수만큼 for문 반복 
#              + move_type=입력받은 방향인 인덱스를 찾고(for문) dx, dy의 해당값을 x,y에 더해준다.
#       3. 좌표를 벗어나는 경우 제외 시킴     

n = int(input())
directions = input().split() # 공백을 기준으로 요소를 구성하는 리스트 형태 반환
x,y = 1,1
# 입력받은 문자열과 이동 방향을 매칭.
dx = [0,0,-1,1] 
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for direction in directions:
    for i in range(len(move_type)):
        if direction == move_type[i]: # 동일한 경우의 인덱스를 이용해 dx,dy 값을 x,y에 더함
            x += dx[i]
            y += dy[i]
    if x<1 or y<1 or x>n or x>n: # 범위를 벗어날때는 이번 회차 이동을 없애고 다음 회차로 넘어감
        continue
print(x,y)


    




