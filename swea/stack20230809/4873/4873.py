import sys
sys.stdin = open('input.txt')

# 4873 / stack / 20230809 / 반복문자 지우기

# 문자열 s 에서 반복된 문잘ㄹ 지우려고 함
# 지워진 부분은 다시 앞뒤를 연결
# 또 반복문자가 생기면 다시 지움
# 남은 문자열의 길이 출력

T = int(input())
for tc in range(1, T+1):
    s = str(input())
    answer = 0

    # stack 맨 처음은 비교가 불가능하기 때문에 넣고 시작
    stack = [0] * len(s)
    stack[0] = s[0]
    top = 0

    # s에 있는 문자 하나씩 stack top와 비교
    for i in range(1, len(s)):
        # 같으면 제거
        if s[i] == stack[top]:
            stack[top] = 0
            top -= 1
        # 다르면 추가
        else:
            top += 1
            stack[top] = s[i]

    answer = top + 1

    print(f'#{tc} {answer}')