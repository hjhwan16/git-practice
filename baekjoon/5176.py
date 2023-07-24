K = int(input())
for i in range(K):
    P, M = map(int, input().split())
    temp = []
    for n in range(P):
        want = int(input())
        temp.append(want)
    print(P - len(set(temp)))
