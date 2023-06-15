# https://www.acmicpc.net/problem/20006
# 23.06.15
# 8:07~8:20

import sys
def solution(input) :
    def find_room(lev,name) :
        for l in rooms :
            if len(l) < M and l[0][0]-10 <= lev and l[0][0]+10 >= lev :
                l.append((lev,name))
                return
        rooms.append([(lev,name)])
    def print_rooms() :
        for l in rooms :
            if len(l) == M :
                print("Started!")
            else :
                print("Waiting!")
            sl = sorted(l, key = lambda x : x[1])
            for i in sl :
                print(i[0], i[1])

    P,M = list(map(int,input().split())) # 플레이어수, 방정원
    rooms = []
    for _ in range(P) :
        lev, name = input().split()
        lev = int(lev)
        find_room(lev,name)
    print_rooms()

input = sys.stdin.readline
solution(input)
