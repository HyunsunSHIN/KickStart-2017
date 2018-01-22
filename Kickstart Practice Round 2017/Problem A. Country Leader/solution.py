# 문제 이름:
# Problem A. Country Leader
# 문제 주소:
# https://code.google.com/codejam/contest/6304486/dashboard



def count_unique_alphabet(str):
    str_witout_space = str.replace(' ','')
    return len(set(str_witout_space))
# set(str) 은 string을 set 으로 변환하는 파이썬 built-in 함수입니다
# 중복되는 알파벳을 중복해서 세지 않도록, set으로 변환한 뒤
# set 내의 원소 갯수를 계산합니다.

t = int(input())
# 여기서 input() 은 한 줄의 인풋을 읽어들입니다.
# 이 때 그 줄의 개행문자 '\n'은 빼고 읽어 들입니다

for i in range(1, t + 1):
  n = input()
  current_leader = ""

  for j in range(int(n)):
      candidate_leader = input()
      if count_unique_alphabet(current_leader) < count_unique_alphabet(candidate_leader):
          current_leader = candidate_leader
      elif (count_unique_alphabet(current_leader) == count_unique_alphabet(candidate_leader)) \
            and (candidate_leader < current_leader):
          current_leader = candidate_leader

  print("Case #{}: {}".format(i, current_leader))
