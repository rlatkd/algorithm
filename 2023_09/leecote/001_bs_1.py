import sys
read = sys.stdin.readline

n, m = map(int, read().split())
array = list(map(int, read().split()))

start = 0
end = max(array)
result = 0

while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)