import math
t = int(input())
# 여기서 input() 은 한 줄의 인풋을 읽어들입니다.
# 이 때 그 줄의 개행문자 '\n'은 빼고 읽어 들입니다

def count(a_b,a,b):
    if a_b <= 0: return 0
    elif a < 0 or b < 0: return 0
    elif b == 0: return math.factorial(a)
    elif a == 0:
        if a_b - b > 0 : return math.factorial(b)
        else: return 0
    else:
        return a*count(a_b+1,a-1,b) + b*count(a_b-1,a,b-1)

for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]
  prob = float(n*count(1,n-1,m))/(math.factorial(n+m))
  print("Case #%i: %.7f" % (i, prob))

