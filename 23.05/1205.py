# https://www.acmicpc.net/problem/1205
# 23.05.29

def solution(input) : 
    N,TS,P = list(map(int,input().split()))
    if N == 0 :
        print(1)
        return
    scores = list(map(int, input().split()))
    
    score_board = [[scores[0],0]]
    for i in scores :
        if i == score_board[-1][0] :
            score_board[-1][1]+=1
        else :
            score_board.append([i,1])

    if N == P and TS <= scores[-1] :
        print(-1)
        return
    
    th = 0
    for s,n in score_board :
        if TS < s :
            th+=n
        else :
            print(th+1)
            return
    print(th+1)
    
solution(input)