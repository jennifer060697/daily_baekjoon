# https://www.acmicpc.net/problem/21921
# 23.06.05

import sys
def solution(input) : 
    # 입력받기
    N,X = list(map(int,input().split()))
    L = list(map(int,input().split()))

    if max(L) == 0 :
        print('SAD')
        return
    
    sums = sum(L[0:X])
    max_sum = sums
    cnt = 1

    for s in range(1,N-X+1) :
        e = s+X-1
        sums = sums-L[s-1]+L[e]
        if max_sum < sums :
            cnt = 1
            max_sum = sums
        elif max_sum == sums :
            cnt+=1
    
    print(max_sum)
    print(cnt)

input = sys.stdin.readline
solution(input)
