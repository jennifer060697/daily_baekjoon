# https://www.acmicpc.net/problem/1806
# 23.05.27

import copy
def solution(input) : 
    # 입력 받기
    N, S = list(map(int,input().split()))
    M = list(map(int,input().split()))

    lp = 0
    rp = 0
    s = M[rp]
    lmin = []
    while True :
        if s >= S : # 부분합이 기준보다 크면
            lmin.append(rp-lp+1)
            lmin = [min(lmin)] # 길이 저장해서 최소 길이 업데이트
            if lmin[0] == 1 : # 1이면 최소길이니까 1 출력 후 종료
                print(1)
                return
            s-=M[lp] # 최소 길이를 업데이트했으면 부분합 수열을 줄여서도 체크해보기 (오른쪽을 줄이는건 이미 체크한 수열임. 왼쪽만 줄여보면 됨)
            lp+=1
        else :
            rp += 1 # 부분합이 기준에 못미치면 오른쪽 늘리기
            if rp >= N : # 수열을 넘어가면 종료
                break
            s += M[rp]

    if len(lmin) :
        print(lmin[0])
    else : # 한번도 목적 달성 못했으면 0
        print(0)

solution(input)