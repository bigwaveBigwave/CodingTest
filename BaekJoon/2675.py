#테스트 케이스만큼 문자열을 입력받으면 각 문자를 R번 반복한 새 문자열을출력하기
#테스트케이스입력받기
#테스트케이스마다 반복문 시작
#반복횟수랑 문자열 입력받기
#문자열의 각 문자마다 반복횟수만큼 늘리고 다시 문자열에 붙이기
#출력

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)

    result = ""
    for ch in S:
        result += ch * R

    print(result, end = " ")