# 4-3책 풀이 
# 푸는 방법: 방향을 지정할 때 x,y 좌표를 한꺼번에 지정=> 튜플형
#            범위에 해당될때만 count 1증가

input_data = input() 
row = int(input_data[1])
column = int(ord(input_data[0]))-96 
count = 0
# 이동가능한 모든 방향 지정
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
for step in steps:
    nextrow = row+step[0] 
    nextcolumn = column+step[1]
    if nextrow >=1 and nextcolumn >=1 and nextrow <=8 and nextcolumn <=8:
        count +=1
    
print(count)