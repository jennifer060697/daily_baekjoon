# https://www.acmicpc.net/problem/21736
# 23.06.08

import sys
sys.setrecursionlimit(10**6)
def solution(input) :
    R,C = list(map(int,input().split()))
    MAP = []
    for _ in range(R) :
        MAP.append(input().strip())
    visit = [[0 for _ in range(C)] for _ in range(R)]
    D = [(1,0),(-1,0),(0,1),(0,-1)]

    def find_I() :
        for r in range(R) :
            for c in range(C) :
                if MAP[r][c] == 'I' : # I P O X
                    return r,c

    def DFS(r,c) :
        if r>=0 and r<R and c>=0 and c<C and visit[r][c] == 0:
            visit[r][c] = 1
            if MAP[r][c] == 'X' :
                return
            if MAP[r][c] == 'P' :
                cnt[0] += 1
            for dr,dc in D :
                DFS(r+dr,c+dc)

    cnt = [0]
    DFS(*find_I())
    if cnt[0] :
        print(cnt[0])
        return
    print('TT')
    

input = sys.stdin.readline
solution(input)
