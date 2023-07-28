# 괄호
import sys
# 입력으로 주어진 괄호 문자열을 확인 후 YES or NO로 나타내기.


T = int(input())
for i in range(T):
    word = sys.stdin.readline().rstrip()
    word_stack = list(word)
    temp = []
    if (word[0] == ")") or (word[-1] == "("):
        print('NO') 
    else:
        for k in range(len(word_stack)):
            temp.append(word_stack.pop())
            if len(temp) >= 2:
                if temp[-2] == ')' and temp[-1] =='(':
                    temp.pop()
                    temp.pop()
            else:
                pass
        if len(temp) == 0:
            print('YES')
        else:
            print('NO')
            


