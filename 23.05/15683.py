# https://www.acmicpc.net/problem/15683
# 23.05.22

import copy
def solution(input) : 
    R,C = list(map(int, input().split()))
    MAP = []
    for _ in range(R) :
        t = list(map(int, input().split()))
        MAP.append(t)

    def count_blind_spot(maps) :
        cnt = 0
        for row in maps :
            for i in row :
                if i == 0 :
                    cnt+=1
        return cnt
    
    def check_right(r,c,maps) :
        for nc in range(c+1,C) :
            if maps[r][nc] == 6 : return
            if maps[r][nc] == 0 : maps[r][nc] = 9
    def check_left(r,c,maps) :
        for nc in range(c-1,-1,-1) :
            if maps[r][nc] == 6 : return
            if maps[r][nc] == 0 : maps[r][nc] = 9
    def check_up(r,c,maps) :
        for nr in range(r-1,-1,-1) :
            if maps[nr][c] == 6 : return
            if maps[nr][c] == 0 : maps[nr][c] = 9
    def check_down(r,c,maps) :
        for nr in range(r+1,R) :
            if maps[nr][c] == 6 : return
            if maps[nr][c] == 0 : maps[nr][c] = 9
    def next_cctv(r,c,maps) :
        for nr in range(r,R) :
            if nr == r : sc = c+1
            else : sc = 0
            for nc in range(sc,C) :
                if maps[nr][nc] in range(1,6) :
                    return (nr,nc)
        return -1
    
    def back_track(cctv,maps) :
        """
        씨씨티비 끝났으면 사각지대 갯수 세서 리턴
        1번 cctv 모든 방향에 대해
            다음 씨씨티비 백트래킹
        백트래킹 결과들에 대해 min 갱신
        """
        if cctv == -1 :
            return count_blind_spot(maps)
        
        r,c = cctv
        n = maps[r][c]
        if n == 1 : check = ((check_right,), (check_up,), (check_left,), (check_down,))
        elif n == 2 : check = ((check_right,check_left,), (check_up,check_down),)
        elif n == 3 : check = ((check_right,check_up), (check_up, check_left,), (check_left,check_down,), (check_down,check_right,))
        elif n == 4 : check = ((check_right, check_up, check_left,), (check_up,check_left,check_down,),(check_left,check_down,check_right,),(check_down,check_right,check_up,))
        elif n == 5 : check = ((check_right,check_up,check_left,check_down,),)

        ncctv = next_cctv(r,c,maps)

        back_track_results = []
        for runs in check :
            nmap = copy.deepcopy(maps)
            for run in runs :
                run(r,c,nmap)
            result = back_track(ncctv, nmap)
            back_track_results.append(result)

        return min(back_track_results)


    cctv = next_cctv(0,-1,MAP)
    print(back_track(cctv, MAP))
    
solution(input)