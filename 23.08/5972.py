'''
Title   : 택배 배송
Link    : https://www.acmicpc.net/problem/5972
Level   : G5
Problem : 노드 1에서 노드 N으로 가는 최단거리를 구한다.
Type    : 그래프 탐색
Idea    : 다익스트라
DATE    : 23.08.12
'''

import heapq
import sys


def solution(input) :
    N,M =  map(int,input().split())
    graph = [
        [] for _ in range(N+1)
    ]

    for _ in range(M) :
        s,e,c = map(int, input().split())
        graph[s].append((e,c))
        graph[e].append((s,c))

    D = [float('inf')]*(N+1)
    
    def dijkstra() :
        D[1] = 0
        q = []
        heapq.heappush(q, (0,1))

        while q :
            d, now = heapq.heappop(q)

            if D[now] < d : continue

            for e,c in graph[now] :
                if D[e] > d+c :
                    D[e] = d+c
                    heapq.heappush(q,(D[e], e))

    dijkstra()
    print(D[N])




input = sys.stdin.readline
solution(input)