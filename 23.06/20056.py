# https://www.acmicpc.net/problem/20056
# 23.06.13
# 10:08~10:56
import sys
def solution(input) :
    N,M,K = list(map(int,input().split()))
    fire_ball = [] # (r,c,m,s,d)
    for _ in range(M) :
        fire_ball.append(list(map(int,input().split())))
    for i in fire_ball : # r,c 를 0부터 시작하게 수정
        i[0]-=1
        i[1]-=1
    D = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] # 주어진 8방향

    def fire_ball_move() : # 끝과 시작이 연결되어있는 상태로 파이어볼 새로운 위치로 옮기기
        nfire_ball = []
        for r,c,m,s,d in fire_ball :
            nr = (r+D[d][0]*s)%N
            nc = (c+D[d][1]*s)%N
            nfire_ball.append((nr,nc,m,s,d))
        return nfire_ball
    
    def add_and_split_fire_ball() : # 한칸에 들어간 파이어볼들을 조건에 맞춰서 합쳤다가 나누기
        nfire_ball = {(r,c):[] for r in range(N) for c in range(N)} # 초기값 세팅
        for r,c,m,s,d in fire_ball : # fire_ball list 를 좌표를 키값으로 갖는 dict로 잠시 이동
            nfire_ball[(r,c)].append([m,s,d])
        
        nlist = [] # 최종 파이어볼 배열
        for r in range(N) :
            for c in range(N) :
                if len(nfire_ball[(r,c)]) == 1 : # 한칸에 하나 들어가있는 경우는 그냥 그대로 최종 배열에 넣기
                    nlist.append((r,c,*nfire_ball[(r,c)][0]))
                elif len(nfire_ball[(r,c)]) > 1 : # 한칸에 두개 이상인 경우
                    msum = 0
                    ssum = 0
                    ds = []
                    flag = 0
                    for m,s,d in nfire_ball[(r,c)] : # m, s의 총합 찾기
                        msum+=m
                        ssum+=s
                        ds.append(d)
                    for d in ds : # 방향 찾기
                        if d%2 != ds[0]%2 :
                            flag = 1
                            break
                            
                    # 파이어볼 합친거 4개로 쪼개기
                    nm = msum//5
                    if nm == 0 :
                        continue

                    ns = ssum//len(nfire_ball[(r,c)])

                    if flag :
                        for nd in [1,3,5,7] :
                            nlist.append((r,c,nm,ns,nd))
                    else :
                        for nd in [0,2,4,6] :
                            nlist.append((r,c,nm,ns,nd))
        return nlist
    
    for _ in range(K) : # K번 마법 수행
        fire_ball = fire_ball_move()
        fire_ball = add_and_split_fire_ball()
    
    msum = 0
    for f in fire_ball : # 남은 질량 총합 구하기
        msum+=f[2]
    print(msum)

input = sys.stdin.readline
solution(input)
