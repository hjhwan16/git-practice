## 스택 = 리스트

#### 1. 스택이란?
  - 가장 나중에 넣은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조로 (Last In First Out) 방식
  - 파이썬에서는 list로 이미 구현

- #### 2. 사용법(내장함수 이용)
  - a_list.append(1): 괄호 안의 요소를 리스트 맨 뒤어 넣음
    ```py
    a_list = [1, 2, 3]
    a_list.append(1)
    print(a_list) # [1, 2, 3, 1]
    ```
  
  - a_list.pop(): 리스트의 맨 뒤에 요소를 꺼내고 리스트에서 삭제함
    ```py
    a_list = [1, 2, 3]
    a_list.pop()
    print(a_list)  # [1, 2]
    ```

#### 3. 클래스를 이용한 스택구현
  ```py
  class stack:
    def __init__(self): # 스택 객체 생성
      self.items = []

    def push(self, item): #스택 요소 추가 push
      self.items.append(item)
    
    def pop(self): # 스택 맨 뒤 요소 삭제하고 리턴
      return self.items.pop()

    def peek(self): # 스택 맨 뒤 요소 리턴
      return self.items[-1]

    def isEmpty(self):
      return not self.items
  

  ```


