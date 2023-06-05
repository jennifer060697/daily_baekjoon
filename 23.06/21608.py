# https://www.acmicpc.net/problem/21608
# 23.06.05

import sys
def solution(input) : 
    # 입력받기
    N = int(input().strip())
    SI = {} # student information : key = student_num, value = likes
    for _ in range(N*N) :
        t = list(map(int,input().split()))
        SI[t[0]] = t[1:]
    SMAP = [[0 for _ in range(N)] for _ in range(N)] # student map

    D = [(1,0),(-1,0),(0,1),(0,-1)] # directions

    def cal_score(r,c,like) : # (r,c) 칸 인근 좋아하는 사람 수, 빈칸 수 계산
        cnt_score = 0
        cnt_zero = 0
        for dr,dc in D :
            nr = r+dr
            nc = c+dc
            if nr >=0 and nr<N and nc>=0 and nc<N :
                if SMAP[nr][nc] in like :
                    cnt_score+=1
                elif SMAP[nr][nc] == 0 :
                    cnt_zero+=1
        return cnt_score,cnt_zero

    def best_spot(like) : # 전체 칸에서 가장 좋은 칸 계산
        # cnt_where = [0,0,0,0] # 0점 ~ 3점, (zeros,r,c)
        best_score = -1
        best_zeros = -1
        sp = (r,c)

        for r in range(N) :
            for c in range(N) : # r 이 작은 순서, c 가 작은 순서대로 탐색
                if SMAP[r][c] : continue # 이미 차있으면 스킵
                score,zeros = cal_score(r,c,like) # 인근 좋아하는사람수, 빈칸수 계산
                if score == 4 : # 4점은 만나는 즉시 종료
                    return r,c
                if best_score < score or (best_score == score and best_zeros < zeros) : # 최고점, 동점일땐 주변 빈칸이 더 많으면 best 갱신
                    best_score, best_zeros, sp = score,zeros,(r,c)
        return sp
        

    def make_SMAP() : # SMAP 채우기
        for n in SI :
            r,c = best_spot(SI[n])
            SMAP[r][c] = n
    
    def cal_sat() : # SMAP 으로 만족도 총점 계산
        score_dict = {
            0:0,
            1:1,
            2:10,
            3:100,
            4:1000
        }
        score = 0
        for r in range(N) :
            for c in range(N) :
                if SMAP[r][c] :
                    s,_ = cal_score(r,c,SI[SMAP[r][c]])
                    score+=score_dict[s]
        return score
    
    make_SMAP()
    print(cal_sat())

input = sys.stdin.readline
solution(input)
