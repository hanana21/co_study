# 탐색: 많은 양의 데이터중 원하는 데이터 찾는 과정 

# 스택 : 박스를 쌓는것과 유사 => 선입 후출(가장 나중에 나온것 먼저 빠진다.)
stack = []
stack.append(5)
stack.append(3)
stack.append(2)
stack.pop()
stack.append(1)
print(stack) # [5,3,1] => 맨나중에 나온게 빠진거 확인 
print(stack[::-1]) # 최상단 부터 출력 

# 큐 : 선입 선출 구조 
from collections import deque #deque 큐와 스택의 장점을 모두 채택=> 빠르고,queue라이브러리보다 간단. 
queue = deque()
queue.append(5)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(1)
print(queue) #deque([3, 2, 1])
queue.reverse()
print(queue)#deque([1, 2, 3]): 나중에 들어온 순서대로 출력 

# 재귀 함수: 자기자신을 다시 호출 => 무한대로 호출은 안된다.(인터프리터 호출 횟수 제한)
#           종료 조건 필요함
#           스택 자료구조 이용(마지막에 호출된것 먼저 끝남)
#           스택 자료구조를 사용해야하는 알고리즘은 재귀함수 이용하면 간편=> DFS
def recursive_function():
    print('재귀함수를 호출')
    recursive_function()
recursive_function()

def recursive_function(i): 
    if i == 100:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료')
recursive_function(1)
