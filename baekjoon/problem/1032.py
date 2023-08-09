# 명령 프롬포트

N = int(input())

for c in range(1, N + 1):
    s = list(str(input()))
    # 맨 처음 값을 ans로 지정
    if c == 1:
        ans = s
    else:
        # 입력된 s를 돌면서 같은 문자면그대로 두고
        # 다른 문자면 ?를 반환
        for i in range(len(s)):
            if s[i] == ans[i]:
                ans[i] = s[i]
            else:
                ans[i] = '?'

for i in ans:
    print(i, end='')    
