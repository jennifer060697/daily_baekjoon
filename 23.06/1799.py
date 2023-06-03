# https://www.acmicpc.net/problem/1799
# 23.06.03

import sys
import time
def solution(input) : 
    N = int(input().strip())
    MAP = []
    for _ in range(N) :
        MAP.append(list(map(int,input().split())))
    RD = [0] * 20 # r+c
    LD = [0] * 20 # r-c+N
    global maxcnt
    maxcnt = 0
    def bt(r,c,cnt,wb) : # wb=0 : 0,0 / wb=1 : 1,0
        global maxcnt
        if r>=N :
            maxcnt = max(maxcnt,cnt)
            return
        if c+2 >= N :
            nr=r+1
            nc=(nr+wb)%2
        else :
            nr=r
            nc=c+2
        
        bt(nr,nc,cnt,wb) # 안놓고 진행

        if MAP[r][c] : # 맵 상 놓을 수 있는 곳
            if RD[r+c] or LD[r-c+N] : # 놓을 수 없다면 끝
                return
            else : # 놓을 수 있다면 놓고 진행
                RD[r+c] = 1
                LD[r-c+N] = 1
                bt(nr,nc,cnt+1,wb)
                RD[r+c] = 0
                LD[r-c+N] = 0

    # 전체 탐색
    # def bt_t(r,c,cnt,wb) : # wb=0 : 0,0 / wb=1 : 1,0
    #     global maxcnt
    #     if r>=N :
    #         maxcnt = max(maxcnt,cnt)
    #         return
    #     nr=r
    #     nc=c+1
    #     if nc>=N:
    #         nr+=1
    #         nc=0
        
    #     bt_t(nr,nc,cnt,wb) # 안놓고 진행

    #     if MAP[r][c] : # 맵 상 놓을 수 있는 곳
    #         if RD[r+c] or LD[r-c+N] : # 놓을 수 없다면 끝
    #             return
    #         else : # 놓을 수 있다면 놓고 진행
    #             RD[r+c] = 1
    #             LD[r-c+N] = 1
    #             bt_t(nr,nc,cnt+1,wb)
    #             RD[r+c] = 0
    #             LD[r-c+N] = 0
    
    F = 0
    bt(0,0,0,0)
    F+=maxcnt
    maxcnt = 0
    bt(0,1,0,1)
    F+=maxcnt
    print(F)

    # bt_t(0,0,0,0)
    # print(maxcnt)


st = time.time()
input = sys.stdin.readline
solution(input)
et = time.time()
print(et-st)