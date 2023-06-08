# https://www.acmicpc.net/problem/17484
# 23.06.08

import sys
def solution(input) :
    R,C = list(map(int,input().split()))
    MAP = []
    for _ in range(R) :
        MAP.append(list(map(int,input().split())))
    
    D = [(1,-1),(1,0),(1,1)]

    fuel_map = [[-1 for _ in range(C)] for _ in range(R)]

    start_points = [(0,i) for i in range(C)]
    last = []

    def DFS(r,c,f,d) :
        if r==R :
            last.append(f)
        if r>=0 and r<R and c>=0 and c<C :
            # if fuel_map[r][c] == -1 or fuel_map[r][c] > f+MAP[r][c] :
            fuel_map[r][c] = f+MAP[r][c]
            for i,(dr,dc) in enumerate(D) :
                if i == d : continue
                DFS(r+dr,c+dc,fuel_map[r][c],i)

    for r,c in start_points :
        DFS(r,c,0,-1)
    print(min(last))


input = sys.stdin.readline
solution(input)
