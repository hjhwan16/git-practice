### 최대공약수 구하는 법
import math
A, B = 10, 20
print(math.gcd(A, B))
 --> 10

### 소숫점 나태나는 법
round(a,b)
 -> a라는 숫자를 소수점 b자리가 남도록 반오림

### 파이썬 입력 빨리 받기
import sys
num = int(sys.stdin.readline().rstrip())

### 이중 리스트 정렬 하기
birthdays.sort(key = lambda x: (x[1], x[2], x[3]))