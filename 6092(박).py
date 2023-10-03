n =int(input())#개수를 입력받아 n에 정수로 저장
a = input().spilt()#공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n):#0부터 n-1까지
  a[i] = int(a[i])#a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []#d라는 이름의 빈 리스트를 만듦.
for i in range(24):#23번 반복
  d.append(0)#[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음

#번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
for i in range(n):
  count_number = d[a[i].count('i')]
#카운트한 값을 공백을 두고 출력-1
for i in range(1, 24):
  print(count_number, end = '')