import sys
input = sys.stdin.readline()

#필요하거나 뺴야하는 수를 각각 출력하기
#배열 입력
# 기준이 되는 배열 선언, 초기화
#반복문 돌려서 필요한 수정 숫자 출력

chess = list(map(int, input().split()))
standard = [1, 1, 2, 2, 2, 8]
for i in range(len(chess)):
    ans = standard[i] - chess[i]
    print(ans)