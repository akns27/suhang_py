#몇 번째 계단인지 입력받음
n = int(input())
# 계단의 숫자를 초기화
stair = [0]*301
#N-1번만큼 반복
for i in range(n):
  stair[i] = int(input())#계단 점수 입력

# dp 배열을 초기화
dp = [0]*301
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

# 점화식을 계산(직전칸에서 올라온 경우, 전전 칸에서 올라온 경우)
for i in range(3, n):#초기값 dp[0], dp[1], dp[2]는 이미 설정되있기때문에 3번째 계단부터 시작
  dp[i] = max(dp[i-3]+ stair[i-1] + stair[i], dp[i-2]+stair[i])#점수 계산(i는 현재 처리 중인 계단의 위치를 나타냄)
#dp 출력
print(dp[n-1])
#https://v3.leedo.me/devs/64