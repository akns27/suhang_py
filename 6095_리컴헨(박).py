# 돌의 개수 n 입력받기
n = int(input())
# 20x20(19x19) 크기의 2차원 리스트 생성 및 0으로 초기화
d = [[0 for i in range(20)]for j in range(20)]
#[0]짜리 칸을 19번 만듦


# 돌을 놓을 좌표 입력받고 바둑판에 1로 표시
for i in range(n):
  x, y = map(int, input().split())
  d[x][y] = 1

# 바둑판 출력
for i in range(1, 20):
  for j in range(1, 20):
    print(d[i][j], end = ' ')
#줄 바꿈
  print()