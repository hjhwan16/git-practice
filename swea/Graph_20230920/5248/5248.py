import sys
sys.stdin = open('input.txt')

def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    # 같은 집합은 보내기
    if x == y:
        return

    # 다른 집합은 같은 대표자로 만들어 주기
    if x < y:
        parent[y] = x
    if y < x:
        parent[x] = y

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N명의 사람 M장의 신청서
    arr = list(map(int, input().split()))
    ans = 0
    parent = [i for i in range(N)] # idx가 첨자 value가 부모
    # print(parent)
    # union을 해준다음 부모의 수를 카운팅 해주면 됨.
    for i in range(M):
        union(arr[2*i]-1, arr[2*i+1]-1)
    # print(parent)
    for i in range(N):
        find_set(i)
    # print(parent)

    ans = len(set(parent))

    print(f'#{tc} {ans}')

