import sys

input = sys.stdin.readline # 더 빨리 입력 받기 

n,m = map(int,input().split())
array = [list(map(int,input().rsplit())) for _ in range(n)] #.rstrip() :문자열 끝의 '\n' 제거
max_value = set()

direction=[   [(0,1),(0,1),(0,1)],
    [(1,0),(1,0),(1,0)],
    # 네모
    [(0,1),(1,0),(0,-1)],
    #L
    [(1,0),(1,0),(0,1)],
    [(1,0),(0,1),(0,1)],
    [(0,1),(1,0),(1,0)],
    [(0,1),(0,-1),(0,-1)],
    [(1,0),(1,0),(0,-1)],
    [(0,1),(0,1),(1,0)],
    [(0,-1),(1,0),(1,0)],
    [(1,0),(0,1),(0,1)],
    #ㄹ
    [(1,0),(1,0),(1,0)],
    [(0,-1),(1,0),(0,-1)],
    [(1,0),(0,-1),(1,0)],
    [(0,1),(1,0),(0,1)],
    # ㅗ
    [(1,0),(1,0),(1,-1)],
    [(1,0),(1,0),(-1,-1)],
    [(1,0),(1,0),(-1,1)],
    [(1,0),(0,1),(0,-2)]
]
def fine_max(x,y):
    for d in direction:
        for j in range(3):
            sum_direction = array[x][y]
            dx = x+d[j][0]
            dy = y+d[j][1]
            if dx <0 or dy <0 or dx>m or dy>n:
                sum_direction = array[x][y]
                break
            else:
                sum_direction += array[dx][dy]
        max_value.add(sum_direction)
        sum_direction = array[x][y]
for i in range (n):
    for j in range(m):
        fine_max(i,j)
print(max(max_value))
