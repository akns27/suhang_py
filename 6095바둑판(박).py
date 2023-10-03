d=[]#대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20):#19번 반복
  d.append([])#리스트 안에 다른 리스트 추가해 넣기
  for j in range(20):#19번 반복
    d[i].append(0)#리스트 안에 들어있는 리스트 안에 0 추가해 넣기
#반복문 i 한 번 돌면 [0]x19 1줄 생성 됨
n = int(input())#흰 돌 n개 
for i in range(n):#n번 반복
  x, y = input().split()#x와 y의 값을 각각 받음
  d[int(x)][int(y)] = 1# x와 y의 위치 하나 하나에 1을 넣어 초기화

for i in range(1, 20):#i만큼 1부터 19까지 반복
  for j in range(1, 20):#j만큼 1에서 19까지 반복
    print(d[i][j], end=' ')#공백을 두고 모든 요소를 출력
  print() #줄 바꿈