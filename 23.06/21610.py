# https://www.acmicpc.net/problem/21610
# 23.06.01

# 10:18 ~ 10:54
import copy
def solution(input) : 
    N,M = list(map(int,input().split()))
    wmap = []
    for _ in range(N) :
        wmap.append(list(map(int,input().split())))
    GO = []
    for _ in range(M) :
        GO.append(tuple(map(int,input().split())))
    D = [(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # 1~8 까지 D

    cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

    def round1(cloud, d, s) :
        dr, dc = D[d][0] * s, D[d][1] * s
        move_cloud = []
        for cr,cc in cloud :
            cr = (cr+dr+N)%N
            cc = (cc+dc+N)%N
            move_cloud.append((cr,cc))
        return move_cloud
    
    def round2(cloud) :
        for cr, cc in cloud :
            wmap[cr][cc] += 1
    
    def round4(b_cloud) :
        for cr,cc in b_cloud :
            cnt = 0
            for dr,dc in [D[2],D[4],D[6],D[8]] :
                nr = cr+dr
                nc = cc+dc
                if nr >= 0  and nr < N and nc >=0 and nc < N :
                    if wmap[nr][nc] >= 1 :
                        cnt += 1
            wmap[cr][cc] += cnt

    def round5(b_cloud) :
        cloud = []
        for r in range(N) :
            for c in range(N) :
                if (r,c) in b_cloud :
                    continue
                if wmap[r][c] >= 2 :
                    cloud.append((r,c))
                    wmap[r][c] -= 2
        return cloud

    def cnt_w() :
        cnt = 0
        for r in range(N) :
            for c in range(N) :
                cnt+=wmap[r][c]
        return cnt
        
    for go in GO :
        cloud = round1(cloud,*go)
        round2(cloud)
        b_cloud = cloud
        round4(b_cloud)
        cloud = round5(b_cloud)

    print(cnt_w())

solution(input)