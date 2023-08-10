# 도키도키 간식드리미 # 20230810

N = int(input())
arr = list(map(int, input().split()))
cnt = 1
stack = []

# arr 도 순회하고 그 때마다 stack 도 순회를 해줘야 함.
for i in arr:
    if i == cnt:
        cnt += 1
        pass
    else:
        stack.append(i)
    if stack:
        for k in range(len(stack)):
            if stack[-1] == cnt:
                stack.pop()
                cnt += 1
            else:
                break


if stack:
    print("Sad")
else:
    print("Nice")