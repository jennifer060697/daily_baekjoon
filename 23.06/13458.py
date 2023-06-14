# https://www.acmicpc.net/problem/13458
# 23.06.14
# 7분
import sys
def solution(input) :
    N = int(input().strip())
    A = list(map(int,input().split()))
    B,C = list(map(int,input().split()))
    cnt = 0
    for a in A :
        cnt+=1
        a-=B
        if 0 < a :
            cnt+=a//C
            if a%C :
                cnt+=1
    print(cnt)

input = sys.stdin.readline
solution(input)
