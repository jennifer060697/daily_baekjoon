# https://www.acmicpc.net/problem/20920
# 23.06.02

import sys
def solution(input) : 
    wdict = {}
    N,M = list(map(int, input().split()))
    for _ in range(N) :
        w = input().strip()
        if len(w) < M :
            continue
        if w in wdict :
            wdict[w] += 1
        else :
            wdict[w] = 1
    wl = list(wdict.keys())
    wl.sort(key = lambda x : (wdict[x] * -1, len(x) * -1, x))

    for i in wl :
        print(i)


input = sys.stdin.readline
solution(input)