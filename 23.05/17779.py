# https://www.acmicpc.net/problem/17779
# 23.05.30

def solution(input) : 
    N = int(input().strip())
    PMAP = []
    for _ in range(N) :
        PMAP.append(list(map(int,input().split())))
    
    min_cal = []
    for d1 in range(1,N) :
        for d2 in range(1,N) :
            for r in range(N) :
                for c in range(N) :
                    gmap = [[0 for _ in range(N)] for _ in range(N)]
                    if r+d1+d2 <= N-1 and 0<=c-d1 and c+d2<=N-1 :
                        g1,g2,g3,g4,g5 = 0,0,0,0,0
                        for rr in range(N) :
                            if rr < r : # 기준점보다 위쪽
                                pl = pr = -1
                            elif rr > r+d1+d2 : # 기준점보다 아래쪽
                                pl = pr = -2
                            elif rr == r : # 기준점
                                pl = pr = c
                                flag1 = 1
                                flag2 = 2
                            elif rr == r+d1+d2 : # 아래쪽 꼭지점
                                pl = pr = c-d1+d2
                                flag1 = 3
                                flag2 = 4
                            else : # 사이에 낀거
                                if rr <= r+d1 :
                                    pl -= 1
                                    flag1 = 1
                                    if rr == r+d1 : flag1 = 3
                                else :
                                    pl += 1
                                    flag1 = 3
                                if rr <= r+d2 :
                                    pr += 1
                                    flag2 = 2
                                else :
                                    pr -= 1
                                    flag2 = 4

                            for cc in range(N) :
                                p = PMAP[rr][cc]
                                if pl == -1 :
                                    if cc <= c :
                                        g1+=p
                                        gmap[rr][cc] = 1
                                        continue
                                    else :
                                        g2+=p
                                        gmap[rr][cc] = 2
                                        continue
                                elif pl == -2 :
                                    if cc < c-d1+d2 :
                                        g3+=p
                                        gmap[rr][cc] = 3
                                        continue
                                    else :
                                        g4+=p
                                        gmap[rr][cc] = 4
                                        continue
                                else :
                                    if cc < pl :
                                        if flag1 == 1 :
                                            g1+=p
                                            gmap[rr][cc] = 1
                                        elif flag1 == 3 :
                                            g3+=p
                                            gmap[rr][cc] = 3
                                        continue
                                    elif pl <= cc and cc <= pr :
                                        g5 += p
                                        gmap[rr][cc] = 5
                                        continue
                                    else :
                                        if flag2 == 2 :
                                            g2+=p
                                            gmap[rr][cc] = 2
                                        elif flag2 == 4 : 
                                            g4+=p
                                            gmap[rr][cc] = 4
                        min_g = min([g1,g2,g3,g4,g5])
                        max_g = max([g1,g2,g3,g4,g5])
                        min_cal.append(max_g - min_g)
                        min_cal = [min(min_cal)]    
        
    print(min_cal[0])
solution(input)