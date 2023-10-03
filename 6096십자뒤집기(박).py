d = []
for i in range(20):
  d.append([])
  for j in range(20):
    d[i].append(0)#여기까지 칸을 만들어 주는 코드

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])#각 칸에 스플릿으로 0과 1을 입력받아 기본 설정하는 코드
  
#바둑판을 20x20으로 만들고, 19번 반복하는 이유는 인덱스가 0번부터 시작해서..

n = int(input())#십자 뒤집기 횟수 입력
for i in range(n) :
  x,y=input().split()#x,y위치 입력받음
  x=int(x)
  y=int(y)
  for j in range(1, 20) :#1~19까지 반복
    if d[j][y]==0 :#0이면 1로 y열 변경
      d[j][y]=1
    else :
      d[j][y]=0#아니면 0 반환

    if d[x][j]==0 :#0이면 1로 x행 변경
      d[x][j]=1
    else :
      d[x][j]=0 #아니면 0 반환

for i in range(1, 20) : #이중 for문 사용
    for j in range(1, 20) :#인덱스가 0에서 시작하니 1부터 19까지
        print(d[i][j], end = ' ')#전부 출력하는 코드
    print( )#줄바꿈