# 정렬 라이브러리 
# - 정렬 알고리즘은 많이 연구된 주제, 어느정도 정립되어있어 외우면 풀수있는 문제 
# - 최악의 경우에도 O(NlogN)보장
# - 정렬 문제 유형 : 정렬라이브러리로 푸는 문제, 원리 묻는 문제, 더 빠른 정렬이 필요한 문제
# 1. sorted() : 퀵 정렬과 비슷한 병합 정렬 기반 
#               퀵 정렬보다는 느리지만 O(NlogN)보장
#               리스트, 딕셔너리 입력받아 -> 리스트로 출력 
# 소스 코드 
array = [7,5,9,0,3,1,6,2,4,8]
print(sorted(array))


# 2.sort(): 리스트 반환X 내부원소 바로 정렬 
# 소스코드 
array.sort()
print(array)

# 튜플 key 정렬
array=[('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]
result = sorted(array,key=setting)
print(result)