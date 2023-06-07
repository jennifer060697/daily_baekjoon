# https://www.acmicpc.net/problem/14940
# 23.06.07

import sys
def solution(input) :
    # 사사오입 반올림 함수 만들기
    def myround(n) :
        if n-int(n) >= 0.5 : return int(n)+1
        else : return int(n)

    # 입력
    N = int(input().strip())

    if N == 0:
        print(N)
        return
    
    # 조건에 맞춰 계산
    L = []
    for _ in range(N) :
        L.append(int(input().strip()))
    cut = myround(N/100*15) # 15% 개수
    L.sort()
    cal = sum(L[cut:N-cut])/(N-2*cut) # 아래 위 cut 잘라서 평균 구하기
    print(myround(cal))

input = sys.stdin.readline
solution(input)
