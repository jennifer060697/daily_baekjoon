# https://www.acmicpc.net/problem/20125
# 23.05.26

def solution(input) : 
    heart = (-1,-1)
    la,ra,back,ll,rl = -1,-1,0,0,0
    N = int(input().strip())
    maps = []
    for _ in range(N) :
        maps.append(input().strip())

    for r in range(N) :
        if '*' not in maps[r] and ll != 0 and rl != 0 :
            break
        if '*' in maps[r] and heart == (-1,-1):
            c = maps[r].index('*')
            heart = (r+1,c)
        elif r == heart[0] :
            arm_start = maps[r].index('*')
            star_cnt = maps[r].count('*')
            la = heart[1] - arm_start
            ra = star_cnt-1-la
        elif la != -1 and maps[r].index('*') == heart[1]:
            back+=1
        elif '*' in maps[r] :
            if maps[r][heart[1]-1] == '*' :
                ll += 1
            if maps[r][heart[1]+1] == '*' :
                rl += 1
    print(heart[0]+1, heart[1]+1)
    print(la,ra,back,ll,rl)

solution(input)