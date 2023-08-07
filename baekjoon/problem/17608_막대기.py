# 모양이 같은 막대기를 일열로 세운 후
# 오른쪽에서 보이는 막대기의 갯수

N = int(input())
# 배열 입력받기
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 1
# 맨 뒤의 값, max_v값 두개 설정
max_v = arr[-1]
last_v = arr[-1]

for num in range(N-2, -1, -1):
    if arr[num] > last_v and arr[num] > max_v:
        ans += 1
        max_v = arr[num]

print(ans)
