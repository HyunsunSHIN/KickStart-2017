import math
t = int(input())
# 여기서 input() 은 한 줄의 인풋을 읽어들입니다.
# 이 때 그 줄의 개행문자 '\n'은 빼고 읽어 들입니다
small = 0;

for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]
  if n <= m:
      small = n
  else:
      small = m
  ans = (small*(small+1))/2
  print("Case #%i: %i" % (i, ans))

