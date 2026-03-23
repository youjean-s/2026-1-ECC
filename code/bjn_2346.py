from collections import deque
n=int(input())
numbers=list(map(int,input().split()))

# (풍선 번호, 풍선 안의 숫자) 형태로 덱 생성
balloons=deque()
for i in range(n):
    balloons.append((i+1, numbers[i]))

result=[]

while balloons:
    # 맨 앞 풍선 터뜨리기
    num, val = balloons.popleft()
    result.append(num)

    if not balloons:
        break

    #남은 풍선 중에서 이동
    #양수: 오른쪽 이동 -> 덱을 "왼쪽으로" 회전
    #음수: 왼쪽 이동 -> 덱을 "오른쪽으로" 회전

    move = (val-1)%len(balloons) #양수 기준으로 정규화
    if val <0:
        move = val % len(balloons) #음수 일 때 재계산
    balloons.rotate(-move)


print(*result)