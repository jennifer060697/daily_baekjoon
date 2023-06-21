# https://www.acmicpc.net/problem/2304
# 23.06.21
# 10:43 ~ 10:58

import sys
from collections import deque
def solution(input) :
    N = int(input().strip())
    MAP = [0]*1001

    maxn = 0 # 첫 기둥 위치
    minn = 10000 #  마지막 기둥 위치
    

    for _ in range(N) : # 첫기둥, 마지막기둥 위치 찾으면서 기둥맵 완성
        n,l = list(map(int,input().split()))
        maxn = max(maxn,n)
        minn = min(minn,n)
        MAP[n] = l

    maxh = max(MAP) # 최고높이
    maxhs = [] # 최고높이 기둥들의 위치
    for i in range(minn, maxn+1) : # 최고 높이 기둥들 위치 찾기
        if MAP[i] == maxh :
            maxhs.append(i)
    
    mintopn = min(maxhs) # 최고 높이 기둥들 중 첫번째
    maxtopn = max(maxhs) # 최고 높이 기둥들 중 마지막

    minarea = 0
    t = 0
    for i in range(minn, mintopn) : # 최고 높이 기둥 전까지 계단식으로 올라가기
        t = max(t,MAP[i])
        minarea+=t

    minarea+=(maxtopn-mintopn+1)*maxh # 최고 높이 기둥 시작 ~ 끝까지는 직사각형

    t = 0
    for i in range(maxn,maxtopn,-1) : # 마지막 최고높이 기둥까지 뒤에서부터 계단식으로 올라가기
        t = max(t,MAP[i])
        minarea+=t

    print(minarea)

input = sys.stdin.readline
solution(input)