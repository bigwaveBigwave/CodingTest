#하노이 탑의 장대들을 세번째 탑으로 옮기는 횟수와 수행 과정을 출력한다

#수도코딩
#원판의 갯수 입력받기(룰 : 큰숫자가 아래에 있어야함)
#스택 필요할듯
#
#나머지 스택의 가장 위쪽값과 지금 스택의 윛쪽 값을비교해서 큰 곳이 있ㅇ면 거기다가

#위쪽값을 옮김. 큰 곳이 없으면 다른 스택을 기준으로 나머지 스택의 위쪽값과 크기 비교.
#종료조건 : 세번째 스택의 크기가 5일때
#
#

N = int(input())
stack1 = []
stack2 = []
stack3 = []
for i in range(N):
    stack1.append(N-i)

while(True) :
    if len(stack3) == N:
        break

    else :
        topOfFirst = stack1.top()
        topOfSecond = stack2.top()
        topOfThird = stack3.top()
        if topOfFirst < topOfSecond :
            stack2.append(topOfFirst)
            stack1.pop()
        else if topOfFirst < topOfThird :
            stack3.append(topOfFirst)


