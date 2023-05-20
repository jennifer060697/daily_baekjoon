# https://www.acmicpc.net/problem/19236
# 23.05.20, 11 AM
import copy
def solution(input) : 
    """
    공간 칸 : (r,c)
    물고기 번호 = 1~16
    방향 8개 : D = []
    물고기 이동. 물고기 번호 오름차순, 이동가능 = 빈칸/다른 물고기가 있는 칸, 이동불가 = 상어, 경계밖
    이동 가능할때까지 반시계 회전, 이동 불가시 이동 x
    다른 물고기가 있으면 자리를 바꿈
    상어이동 (그 방향의 모든 칸으로 이동 가능)
    가능한 모든 경우의 수 계산
    """
    
    # 물고기 정보 받기
    fdict = {} # (방향, 위치)

    def make_pair(li) :
        pairs = []
        for i in range(0,len(li),2) :
            pairs.append((li[i], li[i+1]))
        return pairs
    
    for r in range(4) :
        temp = list(map(int, input().split()))
        for c,p in enumerate(make_pair(temp)) :
            fdict[p[0]] = (p[1]-1, (r,c))

    # 물고기 dict 로 물고기 맵 만들기
    def make_fmap(fdict) :
        fmap = [[0 for _ in range(4)] for _ in range(4)]
        for f in fdict :
            r,c = fdict[f][1]
            fmap[r][c] = f
        return fmap
    
    # 물고기 이동
    def fish_move(fdict) :
        fmap = make_fmap(fdict)
        fish_sorted = list(fdict.keys())
        fish_sorted.sort() # 번호가 작은 순서로 움직인다.
        for f in fish_sorted : # 상어를 제외한 모든 물고기에 대해
            if f == -1 : continue
            (d,(r,c)) = fdict[f]
            for i in range(8) : # 8뱡에 대해서
                nd = (d+i) % 8
                dr, dc = DIR[nd]
                nr, nc = r+dr, c+dc
                # 이동 가능 체크
                if nr >=0 and nr < 4 and nc >= 0 and nc < 4 :# 벽 안에 있나요?
                    if fmap[nr][nc] != -1 : # 상어와 부딪히지 않나요?
                        if fmap[nr][nc] == 0 : # 이동하려는 곳이 빈칸이면 그냥 이동
                            fdict[f] = (nd, (nr,nc))
                        else : # 물고기가 있다면 위치 바꾸기
                            nf = fmap[nr][nc]
                            fdict[nf] = (fdict[nf][0], (r,c))
                            fdict[f] = (nd,(nr,nc))
                        fmap[r][c], fmap[nr][nc] = fmap[nr][nc], fmap[r][c] # 맵 갱신
                        break
        return fdict
    
    # 백트래킹
    def back_track(FDICT, point) :
        max_point = point
        fish_move(FDICT)
        # 상어 이동 경우의 수
        FMAP = make_fmap(FDICT)
        (d, (r,c)) = FDICT[-1]
        dr, dc = DIR[d]
        for i in range(1,5) :
            nr, nc = r + i*dr, c + i*dc
            if nr >= 0 and nr < 4 and nc >= 0 and nc < 4 : # 상어가 벽 안에 있다면
                if FMAP[nr][nc] != 0 : # 먹을 물고기가 있다면
                    n_fdict = copy.deepcopy(FDICT)
                    nf = FMAP[nr][nc]
                    npoint = point + nf
                    n_fdict[-1] = copy.deepcopy(n_fdict[nf])
                    del n_fdict[nf]
                    max_point = max(max_point,back_track(n_fdict, npoint))
            else : break
        return max_point
    
    DIR = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    
    # 상어 입장
    fmap = make_fmap(fdict)
    ff = fmap[0][0]
    fdir = fdict[ff][0]
    fdict[-1] = (fdir, (0,0))
    del fdict[ff]
    # 백트래킹 시작
    max_point = back_track(fdict, ff)

    print(max_point)

solution(input)