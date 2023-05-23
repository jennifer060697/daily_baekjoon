# https://www.acmicpc.net/problem/14890
# 23.05.23

def solution(input) : 
	# 맵 정보 받아오기
    N,L = list(map(int, input().split()))
    MAP = []
    for _ in range(N) :
        MAP.append(list(map(int,input().split())))
    
    # 갈 수 있는 길인지 체크
    def can_go(map) :
    	# 길 표현법 수정
        cmap = [[map[0],0]]
        for i in map :
            if i == cmap[-1][0] :
                cmap[-1][1] += 1
            else :
                cmap.append([i,1])
                
        # 길 가보기
        for i in range(len(cmap)) :
            if i == 0 : continue
            if cmap[i-1][0] == cmap[i][0] + 1 : # 내려가는 경사로
                if cmap[i][1] >= L : cmap[i][1] -= L
                else : return False
            elif cmap[i-1][0] == cmap[i][0] -1 : # 올라가는 경사로
                if cmap[i-1][1] >= L : cmap[i-1][1] -= L
                else : return False
            else : return False
        return True # 걸리는 부분 없이 통과헀으면 성공
    
    MAP_col = [] # 세로길 만들기
    for c in range(N) :
        m = []
        for r in range(N) :
            m.append(MAP[r][c])
        MAP_col.append(m)
	
    # 가로길, 세로길 모두 탐색하기
    cnt = 0
    for m in MAP :
        cnt += can_go(m)
    for m in MAP_col :
        cnt += can_go(m)
    print(cnt)

solution(input)