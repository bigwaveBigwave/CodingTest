#문자열이 vps인지 여부를 출력한다
#문자 하나씩 본다
#├─ '(' → 스택에 넣는다
#├─ ')' → 스택에 '(' 있으면 pop
#│        없으면 즉시 실패
#끝까지 봤다
#├─ 스택 비어 있음 → YES
#└─ 스택 남아 있음 → NO


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    vps = input().strip()
    stack = []
    is_vps = True
    for ch in vps:
        if ch == '(':
            stack.append(ch)
        elif ch == ")":
            if stack:
                stack.pop()
            elif not stack:
                is_vps = False
                break

    if stack:
        is_vps = False

    if is_vps:
        print("YES")
    else:
        print("NO")

