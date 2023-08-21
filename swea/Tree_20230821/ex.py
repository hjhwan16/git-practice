'''
V
부모 자식 ...
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(n):
    if n:   # 존재하는 정점이면
        print(n)        #visit(n)
        preorder(ch1[n])        # 왼쪽
        preorder(ch2[n])        # 오른쪽

def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)



V = int(input())
E = V - 1
arr = list(map(int, input().split()))

# 부모를 인덱스로 자식을 저장
# 자식을 인덱스로 저장

par = [0] * (V+1)
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2 + 1]
    if ch1[p] == 0:     # 자식1이 비어있으면
        ch1[p] = c
    else:
        ch2[p] = c

# 실제 루트 찾기
print(ch1)
print(ch2)
inorder(1)