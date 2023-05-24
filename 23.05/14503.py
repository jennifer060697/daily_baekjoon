# https://www.acmicpc.net/problem/14503
# 23.05.25

def solution(input) : 
    # 입력 받기
    R,C = list(map(int,input().split()))
    r,c,d = list(map(int,input().split()))
    maps = []
    for _ in range(R) :
        maps.append(list(map(int,input().split())))
    D = [(-1,0),(0,1),(1,0),(0,-1)]

    # 로봇청소기 동작
    cnt = 0
    while True :
        if maps[r][c] == 0 : # 청소 안된 칸은 청소하기
            cnt += 1
            maps[r][c] = 2
        flag = 0
        for i in range(4) : # 주변 4칸에 빈칸 있는지만 체크
            nd = (d+i)%4
            dr,dc = D[nd]
            nr,nc = r+dr, c+dc
            if maps[nr][nc] == 0 :
                flag = 1
                break
        if flag : # 빈칸 있으면 90도 회전하고, 회전 후 앞칸이 청소 안한 칸이면 이동
            d = (d+3)%4
            dr,dc = D[d]
            nr,nc = r+dr, c+dc
            if maps[nr][nc] == 0 :
                r,c = nr,nc
                continue
            
        else : # 빈칸 없으면 후진, 벽이면 작동 정지
            dr,dc = D[d]
            r -= dr
            c -= dc
            if maps[r][c] == 1 :
                break
    print(cnt)
            
solution(input)