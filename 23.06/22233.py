# https://www.acmicpc.net/problem/22233
# 23.06.14
# 8분

import sys
def solution(input) :
    N,M = list(map(int,input().split()))
    keyword = set()
    for _ in range(N) :
        keyword.add(input().strip())
    for _ in range(M) :
        keyword -= set(input().strip().split(','))
        print(len(keyword))

input = sys.stdin.readline
solution(input)
