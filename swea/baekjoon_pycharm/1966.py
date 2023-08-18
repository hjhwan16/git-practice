# 프린터 큐
# 조건
# 1. 현재 큐의 가장 앞에 있는 문서의 '중요도'를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 큐 가장 끝에
# 3. 그렇지 않으면 바로 인쇄
'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 문서의 갯수, M: 궁금한 문서의 위치
    arr = list(map(int, input().split()))
    ans = 0
    printQ = []
    for i in range(N):  # [idx, 중요도] 인 수열을 담은 수열을 만듬
        temp = [i, arr[i]]
        printQ.append(temp)

    # idx가 M인 프린트 물이 출력될때까지 출력 -> 순서 저장
    while True:
        # 1. 중요도 확인 printQ[front][1]
        for i in printQ:
            if i[1] > printQ[0][1]:
                temp = printQ.pop(0)
                printQ.append(temp)
                break

        else:
            end_temp = printQ.pop(0)
            ans += 1
            if end_temp[0] == M:
                break
    print(ans)


