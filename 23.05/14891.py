# https://www.acmicpc.net/problem/14891
# 21.05.19 9:03 AM ~ 
def solution(input) : 
    """
    톱니바퀴 번호 = 1, 2, 3, 4
    톱니바퀴 초기 상태 G = [_,1,2,3,4]
    톱니바퀴의 붙어있는 지점 (index) 를 표현한 dict : gi = [12, 21, 23, 32, 34, 43] 이 인덱스를 수정하면서 톱니의 회전을 표현
    """

    # 기어 정보 받아오기 (12시부터 시계방향, N극 = 0, S극 = 1)
    G = [0,]
    for _ in range(4) :
        g = input().strip()
        gi = []
        for t in g :
            gi.append(int(t))
        G.append(gi)
    # 회전수 정보 받아오기
    K = int(input())
    # 회전할 톱니 번호와 방향 받아오기
    R = []
    for _ in range(K) :
        R.append(tuple(map(int, input().split())))
    # 톱니의 회전 상태를 표현해줄 gi 배열 생성
    gi = [2,6,2,6,2,6]

    def rotate(Gn, d) :
        """
        n번 기어를 d 방향으로 회전 (기어의 상호작용은 고려 X)
        """
        d = -d
        if Gn == 1 :
            gi[0]+=d
        elif Gn ==2 :
            gi[1]+=d
            gi[2]+=d
        elif Gn==3 :
            gi[3]+=d
            gi[4]+=d
        else :
            gi[5]+=d
        for i, g in enumerate(gi) :
            if g == 8 :
                gi[i] = 0
            elif g == -1 :
                gi[i] = 7
        
    def check_rotate_gear(M,r) :
        """
        M 번 기어를 r 방향으로 회전할 때 회전될 모든 기어와 방향을 list 로 묶어서 반환
        """
        rg = [(M,r)]
        diff_pole = [G[1][gi[0]] != G[2][gi[1]],
                     G[2][gi[2]] != G[3][gi[3]],
                     G[3][gi[4]] != G[4][gi[5]]]
        if M==1 :
            if diff_pole[0] :
                rg.append((2,-r))
                if diff_pole[1] :
                    rg.append((3,r))
                    if diff_pole[2] :
                        rg.append((4,-r))
        elif M==2 :
            if diff_pole[0] :
                rg.append((1,-r))
            if diff_pole[1] :
                rg.append((3,-r))
                if diff_pole[2] :
                    rg.append((4,r))
        elif M==3 :
            if diff_pole[1] :
                rg.append((2,-r))
                if diff_pole[0] :
                    rg.append((1,r))
            if diff_pole[2] :
                rg.append((4,-r))
        elif M==4 :
            if diff_pole[2] :
                rg.append((3,-r))
                if diff_pole[1] :
                    rg.append((2,r))
                    if diff_pole[0] :
                        rg.append((1,-r))
        return rg
    
    def rotate_all(M,r) :
        """
        M번 기어를 r 방향으로 회전할 때 상호작용을 고려하여 4개 기어를 모두 회전
        """
        rotate_list = check_rotate_gear(M,r)
        for i in rotate_list :
            rotate(*i)

    for r in R :
        rotate_all(*r)

    # 기어들의 12시 방향 극 확인
    gear_12 = [G[1][gi[0]-2], G[2][gi[2]-2], G[3][gi[4]-2], G[4][gi[5]-6]]
    # 점수 계산
    score = [1,2,4,8]
    final_score = 0
    for a,b in zip(gear_12,score) :
        final_score += a*b

    print(final_score)

solution(input)
