"""
n = int(input()) #부른 횟수 n 입력받음
num = input().split()#부른 번호 입력받음
for i in range(n):#n번 반복
  num[i] = int(num[i])#음수, 0번도 들어올 수 있다했으니 num에 정수만 들어오게 만들기
minimum = num[0]#minimum이라는 변수에 num 0번을 집어넣어서 초기화
for j in range(1, n):#1부터 n번 반복(num에 0을 집어넣었기 때문에 1부터 비교)
  if num[j] < minimum:#입력받은 수가 미니멈보다 작으면 
    minimum = num[j]#미니멈에 입력받은 수를 대입

print(minimum)#미니멈=제일 빠른 수 출력
"""



n = int(input())
num = input().split()

for i in range(n):
  num[i] = int(num[i])

minimum = num[0]

for j in range(1, n):
  if num[j] < minimum:
    minimum = num[j]

print(minimum)