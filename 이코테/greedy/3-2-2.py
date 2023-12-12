# 3-2 다른 방법으로 풀기 
# 풀이방법: 가장 큰수와 그다음 큰수만 사용된다는 점을 이용하여 각각의 갯수를 구하자
#           (큰수의 중복 가능 횟수:K + 중복방지용 두번째 큰수 한번 필요) 
#           => 하나의 묶음으로 하여 m에 관한 몫과 나머지로 모두 구할수있다.
#           (m//(K+1))*k + (m%(K+1)) => 가장 큰수의 갯수 
#           m- 가장 큰수 갯수 => 그다음 큰수의 갯수 

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr,reverse=True)

first = arr[0]
second = arr[1]

count_first = (m//(k+1))*k + (m%(k+1))
count_second = m - count_first

result = first * count_first + second * count_second
print(result)
    
            