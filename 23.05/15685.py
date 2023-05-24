# https://www.acmicpc.net/problem/15685
# 23.05.24 수

def solution(input) : 
    # 격자점 0~101
    # 입력과 상수들
    coor = [[0]*101 for _ in range(101)]
    N = int(input().strip())
    dcurves = []
    for _ in range(N) :
        dcurves.append(list(map(int,input().split())))
    D = [(1,0),(0,-1),(-1,0),(0,1)]

    # dc 점들이 들어가면 다음 세대들도 뒤에 붙여주는 함수
    def next_generation(dc_points) :
        cx,cy = dc_points[-1]
        ndc_points = []
        for x,y in dc_points[-2::-1] : # dc 점들 순서 유지를 위해서 마지막부터 거꾸로 추가해줘야함
            nx = cx-y+cy
            ny = cy+x-cx
            ndc_points.append((nx,ny))
        dc_points += ndc_points

    # dc 입력 정보가 들어가면 dc 전체 점들을 만들어주는 함수
    def make_dragoncurve(dc) :
        x,y,d,g = dc
        dx, dy = D[d]
        dc_points = [(x,y), (x+dx, y+dy)]
        for _ in range(g) :
            next_generation(dc_points)
        return dc_points
    
    # dc 전체 점들을 좌표에 찍어줌
    def dc_to_coor(dc_points, coor) :
        for x,y in dc_points :
            coor[x][y] = 1

    # 정사각형 세기
    def cnt_square(coor) :
        cnt = 0
        for x in range(1,101) :
            for y in range(1,101) :
                if coor[x][y] == 1 and coor[x-1][y]== 1 and coor[x][y-1] and coor[x-1][y-1] ==1 :
                    cnt += 1
        return cnt
    
    # main
    for dc in dcurves :
        dc_points = make_dragoncurve(dc)
        dc_to_coor(dc_points, coor)
    
    cnt = cnt_square(coor)

    print(cnt)

solution(input)