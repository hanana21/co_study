import sys

input = sys.stdin.readline # 더빨리 입력받기 
n = int(input())
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 북동남서 

for _ in range(n):
    input_directions = list(input()) # 입력받을 때 str형태로 입력받았고 그걸 list형태로 변환 ['FF','FFLB']
                                     # 만약 int형으로 바꾸고 싶다면 list(map(int,input()))
                                     # "adc" << 얘는 수정 불가 = ['a','d','c'] << 얘는 수정 가능
    x, y, direction = 0, 0, 0  # 초기 위치, 방향
    min_x, min_y, max_x, max_y = 0, 0, 0, 0  # 넓이 구하기용 x, y 
                                             # 초기 위치 0,0 에서 최소값(x)는 왼쪽(-500~0), 최댓값(x)은 오른쪽(0~500)에 무조건 있으므로 기준을 0,0,0,0
                                             # 만약 min_x = 987654321로 한다면 (0,0) -> (1,0) 됐을때 min_x = 0 되야하는데 1이되게되므로 0을 무조건 기준으로 잡을것 
    for i in input_directions:
        if i == 'F':
            x += directions[direction][0]
            y += directions[direction][1]
            min_x = min(min_x, x) # for문안에 걸어버리면 R,L일때도 돌아가니까 낭비
            min_y = min(min_y, y) # 이방식보다 x if x<min_x else min_x (삼항연산자)가 더 빠르다
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        elif i == 'B':
            x -= directions[direction][0]
            y -= directions[direction][1]
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        elif i == 'R':
            direction += 1 
            if direction == 4:
                direction = 0
        elif i == 'L':
            direction -= 1
            if direction == -1:
                direction = 3 
    print(abs(max_x - min_x) * abs(max_y - min_y)) # 굳이 abs 써줄필요는 없다.=> 어짜피 min값은 -니까