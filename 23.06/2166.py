# https://www.acmicpc.net/problem/2166
# 23.06.08

import sys
def solution(input) :
    N = int(input().strip())
    P = []
    for _ in range(N) :
        P.append(tuple(map(int, input().split())))
    P.append(P[0])
    
    sum1 = 0
    sum2 = 0
    for i in range(N) :
        sum1+=P[i][0]*P[i+1][1]
    for i in range(1,N+1) :
        sum2+=P[i][0]*P[i-1][1]
    print(round(abs(sum1-sum2)/2,1))

input = sys.stdin.readline
solution(input)
