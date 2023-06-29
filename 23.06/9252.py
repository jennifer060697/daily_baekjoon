# https://www.acmicpc.net/problem/9252
# 23.06.28

import sys
def solution(input) :
    str1 = '_'+input().strip()
    str2 = '_'+input().strip()


    DP = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

    for i1 in range(1,len(str1)) :
        for i2 in range(1,len(str2)) :
            if str1[i1] == str2[i2] :
                DP[i1][i2] = DP[i1-1][i2-1] + 1
            else :
                DP[i1][i2] = max(DP[i1-1][i2], DP[i1][i2-1])
    
    result = []
    i1 = len(str1)-1
    i2 = len(str2)-1

    print(DP[i1][i2])

    while True :
        if DP[i1][i2] == 0 : break
            
        if DP[i1][i2-1] == DP[i1][i2] :
            i2-=1
            
        elif DP[i1-1][i2] == DP[i1][i2] :
            i1-=1

        else :
            result.append(str1[i1])
            i1-=1
            i2-=1
    
    result.reverse()
    print(''.join(result))
        
input = sys.stdin.readline
solution(input)