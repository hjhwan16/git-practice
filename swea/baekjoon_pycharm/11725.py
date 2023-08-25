'''
7
1 6
6 3
3 5
4 1
2 4
4 7

'''

# 트리의 부모 찾기
import sys
input = sys.stdin.readline
from collections import deque
queue = deque()

N = int(input())
# 자식 노드가 인덱스 부모 노드가 값
ch = [0 for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    if v1 == 1:
        ch[v2] = v1
    # 부모노드가 존재한다면 자식이다
    elif v2 == 1:
        ch[v1] = v2

    else:
        queue.append((v1, v2))

while queue:
    v1, v2 = queue.popleft()

    if ch[v1] != 0:
        ch[v2] = v1

    elif ch[v2] != 0:
        ch[v1] = v2
    else:
        queue.append((v1, v2))




for i in range(2, N+1):
    print(ch[i])


