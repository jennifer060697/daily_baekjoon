# https://www.acmicpc.net/problem/14502

import copy
def solution(input) : 
    R,C = list(map(int,input().split()))
    MAP = []
    for _ in range(R) :
        MAP.append(list(map(int, input().split())))
    
    def next(w) :
        r,c = w
        for nr in range(r,R) :
            if nr == r :
                start = c+1
            else : start = 0
            for nc in range(start,C) :
                if MAP[nr][nc] == 0 :
                    return (nr,nc)
        return -1

    def next_wall() :
        wall[2] = next(wall[2])
        if wall[2] == -1 :
            wall[1] = next(wall[1])
            wall[2] = next(wall[1])
            if wall[2] == -1 :
                wall[0] = next(wall[0])
                wall[1] = next(wall[0])
                wall[2] = next(wall[1])
                if wall[2] == -1 :
                    return -1
                
    def next_virus(w) :
        r,c = w
        for nr in range(r,R) :
            if nr == r :
                start = c+1
            else : start = 0
            for nc in range(start,C) :
                if MAP[nr][nc] == 2 :
                    return (nr,nc)
        return -1
    
    def infection(map) :
        def dfs(map, v) :
            vr,vc = v
            map[v[0]][v[1]] = 3
            dir = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in dir :
                if vr+dr >= 0 and vr+dr < R and vc+dc >= 0 and vc+dc < C :
                    if map[vr+dr][vc+dc] == 0 :
                        nv = (vr+dr, vc+dc)
                        dfs(map,nv)
        
        v = next_virus((0,-1))
        while v != -1 :
            dfs(map,v)
            v = next_virus(v)
        
    def count_safe_zone(map) :
        cnt = 0
        for r in range(R) :
            for c in range(C) :
                if map[r][c] == 0 :
                    cnt+=1
        return cnt
                    
    def calculate_safe_zone() :
        nmap = copy.deepcopy(MAP)
        for wr, wc in wall :
            nmap[wr][wc] = 1
        infection(nmap)
        cnt = count_safe_zone(nmap)
        return cnt
    
    wall = [next((0,-1)), next(next((0,-1))), next(next((0,-1)))]


    cnt = 0
    while next_wall() != -1 :
        ncnt = calculate_safe_zone()
        cnt = max(cnt, ncnt)
    
    print(cnt)

solution(input)
