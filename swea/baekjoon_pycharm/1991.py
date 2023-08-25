import sys
input = sys.stdin.readline

def preorder(p):
    if p:
        print(tree[p], end='')
        preorder(ch1[p])
        preorder(ch2[p])
def inorder(p):
    if p:
        inorder(ch1[p])
        print(tree[p], end='')
        inorder(ch2[p])
def postorder(p):
    if p:
        postorder(ch1[p])
        postorder(ch2[p])
        print(tree[p], end='')


N = int(input())
tree = [0] * (N+1)
data = [0] * (N+1)
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)
for i in range(1, N+1):
    arr = list(input().split())
    tree[int(ord(arr[0]) - 64)] = arr[0]
    if arr[1] != '.':
        ch1[int(ord(arr[0]) - 64)] = ord(arr[1]) - 64
    if arr[2] != '.':
        ch2[int(ord(arr[0]) - 64)] = ord(arr[2]) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)