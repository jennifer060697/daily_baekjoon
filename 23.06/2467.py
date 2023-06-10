# https://www.acmicpc.net/problem/2467
# 23.06.10

import sys
def solution(input) :
    N = int(input().strip())
    L = list(map(int, input().split()))
    mix = (0,0)
    mix_min = 3000000000  
        
    for i in range(N) :
        if L[i] >= 0 :
            if i+1<N and abs(L[i] + L[i+1]) < mix_min :
                mix = (i,i+1)
            break
        
        s = i+1
        e = N-1
        while s<=e :
            mid = (s+e) // 2

            if L[i]+L[mid] == 0 :
                print(L[i],L[mid])
                return
            
            if abs(L[i]+L[mid]) < mix_min :
                    mix_min = abs(L[i]+L[mid])
                    mix = (i,mid)

            if L[i]+L[mid] < 0 :
                s = mid+1
            else :
                e = mid-1
    
    print(L[mix[0]],L[mix[1]])

input = sys.stdin.readline
solution(input)
