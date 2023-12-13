# 문제 : 정수N이 입력 0시0분0초 ~ N시 59분 59초 사이에 3이 하나라도 포함되는 경우의 수 
# 풀이 : 시+분+초를 문자열로 바꿔서 해당 문자열에 3이 존재하는지 확인
#        시분초 for문돌려도 86400가지의 경우의 수 존재함 십만도 안되니까 2초안에 해결 가능 

n = int(input())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1 
print(count)