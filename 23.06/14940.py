# https://www.acmicpc.net/problem/14940
# 23.06.07

import sys
from collections import deque
def solution(input) :
    # bfs, 위치 저장
    # 입력받기
    R,C = list(map(int,input().split()))
    MAP = []
    for _ in range(R) :
        MAP.append(list(map(int,input().split())))

    # 출력용 배열
    dist_map = [[-1 for _ in range(C)] for _ in range(R)]

    # 4방향
    D = [(-1,0),(1,0),(0,-1),(0,1)]

    # 시작 위치 찾고 dist_map 에 0 넣어주기
    def inicialize_and_find_2() :
        r2,c2 = 0,0
        for r in range(R) :
            for c in range(C) :
                if MAP[r][c] == 2 :
                    r2,c2 = r,c
                elif MAP[r][c] == 0 :
                    dist_map[r][c] = 0
        return r2,c2

    # bfs 돌면서 dist_map 채우기
    def bfs(r,c) :
        deq = deque([(r,c,0)]) # r, c, level
        dist_map[r][c] = 0

        while deq :
            r,c,lev = deq.popleft()
            for dr, dc in D :
                nr = r+dr
                nc = c+dc
                if nr >= 0 and nr < R and nc >= 0 and nc < C :
                    if MAP[nr][nc] == 1 and dist_map[nr][nc] == -1 :
                        dist_map[nr][nc] = lev+1
                        deq.append((nr,nc,lev+1))
    
    r,c = inicialize_and_find_2()
    bfs(r,c)

    # 출력
    for r in range(R) :
        print(' '.join(str(i) for i in dist_map[r]))

input = sys.stdin.readline
solution(input)
