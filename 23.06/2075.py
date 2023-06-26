# https://www.acmicpc.net/problem/2075
# 23.06.26
# 6:52 ~ 
import sys
import heapq
def solution(input) :
    # 최소힙, 원소 N 개를 항상 유지
    # 모든 내용물을 다 넣었을때 head 가 우리가 구하고자하는 값이 됨

    H = []

    N = int(input().strip())
    
    cnt = 0
    for _ in range(N) :
        for n in list(map(int,input().split())) :
            heapq.heappush(H, n)
            cnt+=1
            if cnt > N :
                heapq.heappop(H)
    print(heapq.heappop(H))

        
input = sys.stdin.readline
solution(input)