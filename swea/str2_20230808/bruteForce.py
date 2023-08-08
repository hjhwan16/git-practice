# Target: 검색대상 // Pattern: 검색패턴

target = "SSAFY 10th Let's go"
pattern = "go"


def bruteForce(pattern, target):
    N = len(target) # 검색대상의 길이
    M = len(pattern) # 검색패턴의 길이
    
    i = 0 # target의 인덱스
    j = 0 # pattern의 인덱스

    # 반복을 돌아야지
    while j < M and i < N:
        # 패턴과 다른 곳을 발견 했을 때
        if target[i] != pattern[j]:
            # j만큼 온 상태에서 틀린 곳을 발견함.
            # i: 지금위치 - j
            i = i - j
            # j: 처음으로, 이유: 패턴과 일치하는 문자열이 발견 됐을 때, j+1을 해주기 때문
            j = -1
            
        # 패턴과 같은 곳을 발견 했을 때
        i = i + 1
        j = j + 1
    
    if j == M:
        # 패턴 인덱스 j가 패턴의 길이 만큼 탐색 된 것. --> 탐색 성공
        return i - M
    else:
        return - 1
