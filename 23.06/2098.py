# https://www.acmicpc.net/problem/2098
# 외판원 순회 TSP Traveling Salesman Problem
# 23.06.15
# 8:33~9:33
import sys
def solution(input) :
    N = int(input().strip())
    mini = [[0 for _ in range(2**N)] for _ in range(N)] #[현위치][조합],남은 길 최소비용
    # 출발 노드 0, 다 들르고 다시 0으로 돌아가는 케이스의 남은 길 최소비용
    COST = []
    for _ in range(N) :
        COST.append(list(map(int,input().split())))
    for i in range(N) :
        mini[i][-1] = COST[i][0]

    def dfs(now,visit) :
        if mini[now][visit] : # 남은 길 최소비용이 정해진 경우
            return mini[now][visit]
        mc = 999999999999
        for n in range(N) : # 다음 들를 곳은
            if 1<<n & visit : continue # 이미 들렀던 곳이면 패쓰
            dcost = COST[now][n] # 다음 비용
            if dcost == 0 : continue # 0원 길은 없는 길
            mc = min(mc,dfs(n,visit+(1<<n))+dcost)
        mini[now][visit] = mc
        return mc
    
    print(dfs(0,1))


input = sys.stdin.readline
solution(input)
