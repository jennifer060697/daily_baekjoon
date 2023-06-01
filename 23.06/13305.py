# https://www.acmicpc.net/problem/13305
# 23.06.01

def solution(input) : 
    N = int(input().strip())
    R = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    # 시간초과 
    # def recur(road, cost) :
    #     fcost = 0
    #     if len(cost) <= 0 : return fcost
    #     midx = cost.index(min(cost))
    #     c = cost[midx]
    #     min_c_dist = sum(road[midx:])
    #     fcost += c*min_c_dist
    #     fcost += recur(road[:midx],cost[:midx])
    #     return fcost

    # print(recur(R,C[:-1]))

    min_c = C[0]
    fcost = 0
    m = 0
    for i in range(N-1) :
        if min_c > C[i] :
            fcost += m*min_c
            min_c = C[i]
            m = R[i]
        else :
            m+=R[i]
    fcost += min_c*m
    print(fcost)

solution(input)