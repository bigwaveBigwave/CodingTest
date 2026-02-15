#구하는 것 : "666"이 연속으로 포함된 수를 작은 수부터 나열했을 때 N번째 수를 출력하기
#구조화
# n 입력받기
# 올라가는 숫자, 번째 변수 필요
# num = 666
# str(num)안에 숫자가 있으면 카운트 + 1
# 카운트가 N이 되면 num을 출력하고 종료
# 카운트가 N이 아니라면 num + 1
import sys
input = sys.stdin.readline
n = int(input())
num = 666 #숫자
count = 0 #번째
while True:
    if "666" in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1