# 줄 세우기 / 20230824
import sys
sys.stdin = open('input.txt')

# 한명씩 세우면서 자기 앞에 키가 큰학생이 있으면 바로 앞에 서기. A 부터 그 뒤의 모든 학생들은 한발씩 뒤로 물러섬
# 이 과정을 반복함

T = int(input())
for tc in range(1, T+1):
    t, *arr = map(int, input().split())
    # 맨 앞에 버퍼 칸 하나 설정
    arr = [0] + arr
    ans = 0
    for i in range(2, 21):
        n = 0 + i
        while True:
            # 제대로 들어감
            if arr[n-1] < arr[n]:
                break
            # 자리바꾸는 경우 총 i명 존재 얘는 n 번 째
            else:
                # print(arr[n-1], arr[n], i, n)
                arr[n-1], arr[n] = arr[n], arr[n-1]
                n -= 1
                # 멈추는 경우에만 뒷 사람 수 만큼 카운트
                if arr[n - 1] < arr[n]:
                    ans += (i-n)
                if n < 0:
                    break
    print(t, ans)
