import heapq
import sys
input = sys.stdin.readline
# N = int(sys.stdin.readline())
N = int(input())    # 연산의 수
heap = []
for _ in range(N):
    x = int(input())    # 입력값 자연수라면 힙에 추가 / 0이라면 pop
    if x == 0:
        if heap:
            result = heapq.heappop(heap)
            print(result)
        else:
            print(0)
    else:
        heapq.heappush(heap, x)

'''
9
0
12345678
1
2
0
0
0
0
32

'''