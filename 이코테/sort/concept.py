# 정렬: 데이터를 특정 기준을 따라 순서대로 나열하는 것 
#       가장 많이 사용되는 알고리즘 
#       이진 탐색 가능해짐 
#       면접 단골, 매우 중요한 알고리즘 

# 1. 선택 정렬
#    : 가장 작은 것을 선택하는 알고리즘
#      => 정렬되지 않은 데이터중 가장 작은 데이터를 첫번째 요소와 비교해 작으면 바꾸고  
#         그다음 정렬되지 않은 데이터중 가장 작은 데이터를 두번째 요소와 비교해 작으면 바꾸고,,,,,,,,,
#     - N개의 요소를 정렬 한다면 총 N-1번 진행
#     - 시간 복잡도 N(O2): 데이터가 10,000개 넘어가면 비효율적 
#     - 특정 리스트에서 가장 작은 데이터 찾는 일이 빈번하니 형태에 익숙해 질것 
#      
# 선택 정렬 소스 코드
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index],array[i]=array[i],array[min_index] # 스와프
print(array)

# 2. 삽입 정렬 
#    : 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
#    => 두번째 데이터 부터 시작(첫번째는 이미 정렬되있다 판단)
#       두번째 데이터부터 들어갈 자리 판단하여 삽입(자기 이전의 데이터들은 이미 정렬된 상태)
#    - 선택 정렬 보다는 시간적으로 효율적 
#    - 필요할 떄만 자리 바꿈(선택정렬은 모두 확인하고 바꾼다.) => 이미 정렬된 상태면 효율적
#    - 시간 복잡도 N(O2) => 이미 정렬된 상태면 매우 빠르다(N(O)시간복잡도 가질수도, 퀵정렬보다 빠를수도)
# 삽입정렬 소스코드 
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
    for j in range(i,0,-1): # i부터 1까지 -1씩 감소하며 반복문 진행
        if array[j]<array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break # 이미 자기 앞은 데이터가 오름차순으로 정렬된 상태라 자기보다 작은데이터 찾으면 거기가 자리임
print(array)
