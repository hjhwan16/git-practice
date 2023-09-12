N = int(input())
arr = list(map(int, input().split()))
avail_cost = int(input())

if sum(arr) <= avail_cost :
  print(max(arr))
  exit()

answer = 0
start, end = 0, avail_cost
while start <= end:
  mid = (start + end) // 2
  temp = 0
  for need in arr:
    temp += need if need < mid else mid

  if temp <= avail_cost:
    answer = max(answer, mid)
    start = mid+1
  else :
    end = mid-1

print(answer)