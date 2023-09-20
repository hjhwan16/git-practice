# 1 ~ 10
# make set
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]

# find set
def find_set(x):
    if parent[x] == x:
        return x

    return find_set(parent[x])

# union
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y