#문자열을 입력받으면 문자열의 첫글자와 마지막 글자 출력하기
#테케입력
#테케만큼 반복
#문자열의 첫글자와 마지막 글자를 연속해서 출력
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a = input().strip()
    while a =="":
        a = input().strip()
    print(a[0] + a[-1])
