# 큐스택
import sys
input = sys.stdin.readline
# N개의 자료 구조가 나열 각각의 자료구조에는 한개의 원소가 들어 있음

N = int(input())
A = list(map(int, input().split()))     # Ai가 0인경우 큐, Ai가 1인 경우 스택
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = []
# 스택인 경우 들어갔다가 그대로 나옴
# 큐인 경우 바꿔줌
for i in range(N-1, -1, -1):
    if A[i] == 0:
        queue.append(B[i])

queue = queue + C

for i in range(M):
    print(queue[i], end=' ')


