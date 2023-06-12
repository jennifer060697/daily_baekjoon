# https://www.acmicpc.net/problem/16234
# 23.06.13

import sys
sys.setrecursionlimit(100000)
def solution(input) :
    N,L,R = list(map(int,input().split()))
    population_map = []
    for _ in range(N) :
        population_map.append(list(map(int,input().split())))
    D = [(-1,0),(1,0),(0,-1),(0,1)]

    def dfs(r,c,g) :
        if visit[r][c] : # 들른적 있으면
            return
        visit[r][c] = g
        for dr,dc in D :
            nr = r+dr
            nc = c+dc
            if nr>=0 and nr<N and nc>=0 and nc<N and abs(population_map[r][c]-population_map[nr][nc]) >= L and  abs(population_map[r][c]-population_map[nr][nc]) <= R:
                dfs(nr,nc,g)

    def open_border() :
        g = 0
        for r in range(N) :
            for c in range(N) :
                if visit[r][c] :
                    continue
                else :
                    g+=1
                    dfs(r,c,g)
        if g == N*N : # 경계가 하나도 안열린경우
            return -1
        else :
            return g
    
    def population_move(g) :
        pop_dict = {
            gn : {
                'pop_sum' : 0,
                'pop_count' : 0,
                'points' : []
            }
            for gn in range(1,g+1)
        }

        for r in range(N) :
            for c in range(N) :
                g = visit[r][c]
                pop_dict[g]['pop_sum'] += population_map[r][c]
                pop_dict[g]['pop_count'] += 1
                pop_dict[g]['points'].append((r,c))

        for gn in pop_dict :
            n_pop = pop_dict[gn]['pop_sum'] // pop_dict[gn]['pop_count']
            for r,c in pop_dict[gn]['points'] :
                population_map[r][c] = n_pop

    cnt = 0
    while True :
        visit = [[0 for _ in range(N)] for _ in range(N)]
        g = open_border()
        if g == -1 :
            print(cnt)
            return
        else :
            cnt+=1
            population_move(g)

input = sys.stdin.readline
solution(input)
