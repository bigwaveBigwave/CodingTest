#모두 회전시킨 이후에 네 톱니바퀴의 12시 방향의 점수의 합을 출력
#총 네개 톱니바퀴, 8개의 극(N= 0, S = 1), 12시부터 시계바향
#ㅗ회전횟수
#회전횟수 만큼 회전시킬방법이 각 줄마다 입력
#회전 횟수마큼의 각 줄마다 하나는 회전 바퀴으 번호, 하나는 방향
import sys
input = sys.stdin.readline

#입력받기
arr = []
for _ in range(4):
    arr.append(list(int, input()))

for _ in range(int(input())):
    rotation, dir = map(int, input().split())
    # 회전하기(극이 같으면 회전안함, 극이 다르면 반대방향으로 회전)
    rotation = rotation - 1
    if rotation == 1:
        #극의 방향 두개
        if arr[rotation][2] == arr[rotation+1][6] :



#점수 출력하기
answer = 0#이거 선언 안 하면 왜 오류나지?
for i in range(4):
    answer += arr[i][0]

print(answer)