# 문제: 8x8 평면상에서 나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수?
#      (L자 형태로만 이동 가능)
# 풀이방법: 1. 방향을 지정하기 (L형태로 갈수있는 경우들 정리)
#           2. 입력받은 위치를 int로 변환하고 가능한 방향 카운트
#              만약 벗어난다면 카운트 제외한다.

input_data = input() # 출력값 문자열, split()하면 리스트로 출력됨
row = int(input_data[1])
column = int(ord(input_data[0]))-96 # ord()은 아스키코드로 변환하는 함수 -96은 'a=97'이기 때문
count = 0
# 이동가능한 모든 방향 지정
dx = [2,2,1,-1,-2,-2,-1,1]
dy = [-1,1,2,2,-1,1,-2,-2]
for i in range(len(dx)):
    nextrow = row+dx[i] # 경우의 수를 확인하기 위해서는 처음위치 값은 그대로여야하니까 원래값에 더하지 말고 새로운 객체 만들어주자
    nextcolumn = column+dy[i]
    if nextrow <1 or nextcolumn <1 or nextrow >8 or nextcolumn >8:
        continue # continue아래부터는 코드 무시하고 다음회차로 넘어감 
    count +=1
    
print(count)