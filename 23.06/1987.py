# https://www.acmicpc.net/problem/1987
# 23.06.04

import sys
def solution(input) : 
    # 입력받기
    R,C = list(map(int,input().split()))
    M = []
    for _ in range(R) :
        M.append(input().strip())
    # A~Z 중 들른 알파벳 체크
    check_list = [0] * 26
    # 알파벳 to list index
    def alph_to_asci(a) :
        return ord(a)-ord('A')
    # 4방향
    D = [(-1,0),(1,0),(0,-1),(0,1)]

    # 백트래킹
    def backtrack(r,c,check_list,cnt,maxcnt) :
        k = alph_to_asci(M[r][c])
        if check_list[k] : # 들렀던 알파벳이면 종료
            maxcnt = max(cnt,maxcnt)
            return maxcnt
        
        check_list[k] = 1
        cnt+=1
        for dr,dc in D :
            nr = r+dr
            nc = c+dc
            if nr>=0 and nr<R and nc>=0 and nc<C :
                maxcnt = backtrack(nr,nc,check_list,cnt,maxcnt)
        check_list[k] = 0
        return maxcnt
    
    print(backtrack(0,0,check_list,0,0))

input = sys.stdin.readline
solution(input)
